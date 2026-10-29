"""Batch gradient descent for ordinary least-squares linear regression."""

from typing import List, Sequence, Tuple


def batch_gradient_descent(
	X: Sequence[Sequence[float]],
	y: Sequence[float],
	learning_rate: float = 0.01,
	iterations: int = 1000,
) -> Tuple[List[float], float, List[float]]:
	"""Train a linear model using the complete dataset for each update.

	Returns ``(weights, bias, loss_history)``.
	"""
	if not X or len(X) != len(y):
		raise ValueError("X and y must have the same non-zero length")
	if learning_rate <= 0 or iterations < 0:
		raise ValueError("learning_rate must be positive and iterations non-negative")

	feature_count = len(X[0])
	if feature_count == 0 or any(len(row) != feature_count for row in X):
		raise ValueError("all samples must have the same non-zero number of features")

	weights = [0.0] * feature_count
	bias = 0.0
	sample_count = len(X)
	losses: List[float] = []

	for _ in range(iterations):
		errors = [
			sum(weight * feature for weight, feature in zip(weights, row))
			+ bias
			- target
			for row, target in zip(X, y)
		]
		losses.append(sum(error * error for error in errors) / sample_count)

		for index in range(feature_count):
			gradient = sum(error * row[index] for error, row in zip(errors, X))
			weights[index] -= learning_rate * 2 * gradient / sample_count
		bias -= learning_rate * 2 * sum(errors) / sample_count

	return weights, bias, losses


if __name__ == "__main__":
	weights, bias, _ = batch_gradient_descent(
		[[1], [2], [3], [4]], [2, 4, 6, 8]
	)
	print(f"weights={weights}, bias={bias:.4f}")
