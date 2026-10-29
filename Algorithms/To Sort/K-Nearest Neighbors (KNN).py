"""A simple implementation of the k-nearest neighbors classifier."""

from collections import Counter
from math import dist


class KNearestNeighbors:
	"""Classify points using the labels of their nearest training points."""

	def __init__(self, k=3):
		if k < 1:
			raise ValueError("k must be at least 1")
		self.k = k
		self._points = []
		self._labels = []

	def fit(self, points, labels):
		"""Store the training points and corresponding labels."""
		points = list(points)
		labels = list(labels)
		if not points or len(points) != len(labels):
			raise ValueError("points and labels must be non-empty and equal in length")
		dimensions = len(points[0])
		if any(len(point) != dimensions for point in points):
			raise ValueError("all points must have the same number of features")
		self._points = points
		self._labels = labels
		return self

	def predict(self, points):
		"""Return the majority label among each point's nearest neighbors."""
		if not self._points:
			raise ValueError("fit the classifier before predicting")

		neighbor_count = min(self.k, len(self._points))
		predictions = []
		for point in points:
			distances = sorted(
				(dist(point, training_point), label)
				for training_point, label in zip(self._points, self._labels)
			)
			nearest_labels = [label for _, label in distances[:neighbor_count]]
			counts = Counter(nearest_labels)
			predictions.append(min(counts, key=lambda label: (-counts[label], str(label))))
		return predictions


if __name__ == "__main__":
	classifier = KNearestNeighbors(k=3).fit(
		[(1, 1), (1, 2), (4, 4), (5, 4)],
		["red", "red", "blue", "blue"],
	)
	print(classifier.predict([(2, 2), (4, 3)]))
