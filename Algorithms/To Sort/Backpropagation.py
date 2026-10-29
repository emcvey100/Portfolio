"""A small, dependency-free implementation of backpropagation.

The network has one hidden layer and uses sigmoid activations with mean
 squared-error loss.  ``train`` returns the loss after every epoch.
"""

from math import exp
from random import Random


def sigmoid(value):
    """Return the sigmoid activation, with protection against overflow."""
    if value < 0:
        value = exp(value)
        return value / (1 + value)
    return 1 / (1 + exp(-value))


def sigmoid_derivative(output):
    """Derivative of sigmoid, expressed in terms of its output."""
    return output * (1 - output)


class NeuralNetwork:
    """A fully connected network with one hidden layer."""

    def __init__(self, input_size, hidden_size, output_size, seed=0):
        if min(input_size, hidden_size, output_size) <= 0:
            raise ValueError("layer sizes must be positive")

        random = Random(seed)
        scale = 1 / (input_size ** 0.5)
        self.weights_input_hidden = [
            [random.uniform(-scale, scale) for _ in range(input_size)]
            for _ in range(hidden_size)
        ]
        self.bias_hidden = [0.0] * hidden_size
        scale = 1 / (hidden_size ** 0.5)
        self.weights_hidden_output = [
            [random.uniform(-scale, scale) for _ in range(hidden_size)]
            for _ in range(output_size)
        ]
        self.bias_output = [0.0] * output_size

    def _forward(self, inputs):
        hidden = [
            sigmoid(sum(weight * value for weight, value in zip(row, inputs)) + bias)
            for row, bias in zip(self.weights_input_hidden, self.bias_hidden)
        ]
        output = [
            sigmoid(sum(weight * value for weight, value in zip(row, hidden)) + bias)
            for row, bias in zip(self.weights_hidden_output, self.bias_output)
        ]
        return hidden, output

    def predict(self, inputs):
        """Return the network's output for one input vector."""
        return self._forward(inputs)[1]

    def train(self, samples, targets, learning_rate=0.5, epochs=1000):
        """Train on matching input/target vectors and return epoch losses."""
        if len(samples) != len(targets) or not samples:
            raise ValueError("samples and targets must be non-empty and equal in length")
        history = []
        for _ in range(epochs):
            loss = 0.0
            for inputs, target in zip(samples, targets):
                hidden, output = self._forward(inputs)
                errors = [prediction - expected for prediction, expected in zip(output, target)]
                loss += sum(error * error for error in errors) / len(errors)

                output_delta = [
                    error * sigmoid_derivative(prediction)
                    for error, prediction in zip(errors, output)
                ]
                hidden_delta = [
                    sigmoid_derivative(value) * sum(
                        row[index] * delta
                        for row, delta in zip(self.weights_hidden_output, output_delta)
                    )
                    for index, value in enumerate(hidden)
                ]

                for index, delta in enumerate(output_delta):
                    for hidden_index, value in enumerate(hidden):
                        self.weights_hidden_output[index][hidden_index] -= learning_rate * delta * value
                    self.bias_output[index] -= learning_rate * delta
                for index, delta in enumerate(hidden_delta):
                    for input_index, value in enumerate(inputs):
                        self.weights_input_hidden[index][input_index] -= learning_rate * delta * value
                    self.bias_hidden[index] -= learning_rate * delta
            history.append(loss / len(samples))
        return history


if __name__ == "__main__":
    # XOR example
    network = NeuralNetwork(2, 4, 1, seed=1)
    network.train([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]])
    for sample in ([0, 0], [0, 1], [1, 0], [1, 1]):
        print(sample, network.predict(sample)[0])
