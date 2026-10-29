"""A dependency-free binary linear Support Vector Machine."""


class SVM:
	"""Train a linear SVM using stochastic sub-gradient descent."""

	def __init__(self, learning_rate=0.001, regularisation=0.01, epochs=1000):
		if learning_rate <= 0 or regularisation < 0 or epochs < 1:
			raise ValueError("invalid training parameters")
		self.learning_rate = learning_rate
		self.regularisation = regularisation
		self.epochs = epochs
		self.weights = None
		self.bias = 0.0
		self.classes_ = None

	def fit(self, X, y):
		"""Fit the classifier. X contains numeric rows and y has two classes."""
		X = [list(row) for row in X]
		y = list(y)
		if not X or len(X) != len(y) or not X[0]:
			raise ValueError("X and y must be non-empty and have equal length")
		width = len(X[0])
		if any(len(row) != width for row in X):
			raise ValueError("all rows in X must have the same length")
		self.classes_ = list(dict.fromkeys(y))
		if len(self.classes_) != 2:
			raise ValueError("SVM requires exactly two classes")

		targets = [1 if label == self.classes_[1] else -1 for label in y]
		self.weights = [0.0] * width
		self.bias = 0.0
		for _ in range(self.epochs):
			for row, target in zip(X, targets):
				margin = target * (self._dot(row) + self.bias)
				if margin >= 1:
					gradient = [self.regularisation * weight
								for weight in self.weights]
					bias_gradient = 0.0
				else:
					gradient = [self.regularisation * weight - target * value
								for weight, value in zip(self.weights, row)]
					bias_gradient = -target
				self.weights = [weight - self.learning_rate * change
								for weight, change in zip(self.weights, gradient)]
				self.bias -= self.learning_rate * bias_gradient
		return self

	def _dot(self, row):
		return sum(weight * value for weight, value in zip(self.weights, row))

	def decision_function(self, X):
		"""Return signed distances from the separating hyperplane."""
		if self.weights is None:
			raise ValueError("fit the SVM before making predictions")
		return [self._dot(row) + self.bias for row in X]

	def predict(self, X):
		"""Predict the original class labels."""
		return [self.classes_[1] if score >= 0 else self.classes_[0]
				for score in self.decision_function(X)]

	def score(self, X, y):
		"""Return classification accuracy."""
		y = list(y)
		predictions = self.predict(X)
		if len(predictions) != len(y) or not y:
			raise ValueError("X and y must be non-empty and have equal length")
		return sum(prediction == actual
				   for prediction, actual in zip(predictions, y)) / len(y)
