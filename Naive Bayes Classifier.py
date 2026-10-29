"""A small Gaussian Naive Bayes classifier implemented from scratch."""

from collections import Counter
from math import exp, log, pi, sqrt


class NaiveBayesClassifier:
	"""Classify rows containing continuous numerical features."""

	def __init__(self, smoothing=1e-9):
		self.smoothing = smoothing
		self.classes = []
		self.priors = {}
		self.means = {}
		self.variances = {}

	def fit(self, X, y):
		if not X or len(X) != len(y):
			raise ValueError("X and y must be non-empty and have equal lengths")

		self.classes = list(dict.fromkeys(y))
		counts = Counter(y)
		feature_count = len(X[0])
		if any(len(row) != feature_count for row in X):
			raise ValueError("All rows in X must have the same length")

		for label in self.classes:
			rows = [row for row, target in zip(X, y) if target == label]
			self.priors[label] = counts[label] / len(y)
			self.means[label] = [sum(row[i] for row in rows) / len(rows)
								  for i in range(feature_count)]
			self.variances[label] = [
				max(sum((row[i] - self.means[label][i]) ** 2 for row in rows)
					/ len(rows), self.smoothing)
				for i in range(feature_count)
			]
		return self

	def _log_probability(self, row, label):
		probability = log(self.priors[label])
		for value, mean, variance in zip(
				row, self.means[label], self.variances[label]):
			probability += -0.5 * log(2 * pi * variance)
			probability -= (value - mean) ** 2 / (2 * variance)
		return probability

	def predict_one(self, row):
		if not self.classes:
			raise ValueError("The classifier must be fitted before prediction")
		return max(self.classes, key=lambda label: self._log_probability(row, label))

	def predict(self, X):
		return [self.predict_one(row) for row in X]


if __name__ == "__main__":
	X = [[1.0, 1.1], [1.2, 0.9], [4.0, 4.2], [3.8, 3.9]]
	y = ["small", "small", "large", "large"]
	classifier = NaiveBayesClassifier().fit(X, y)
	print(classifier.predict([[1.1, 1.0], [4.1, 4.0]]))
