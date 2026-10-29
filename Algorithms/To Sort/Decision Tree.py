"""A small decision-tree classifier implemented without external dependencies."""

from collections import Counter
from math import log2


class _Node:
	def __init__(self, *, prediction=None, feature=None, threshold=None,
				 left=None, right=None):
		self.prediction = prediction
		self.feature = feature
		self.threshold = threshold
		self.left = left
		self.right = right


class DecisionTree:
	"""Binary decision tree using information gain for numeric features."""

	def __init__(self, max_depth=None, min_samples_split=2):
		if max_depth is not None and max_depth < 0:
			raise ValueError("max_depth must be non-negative or None")
		if min_samples_split < 2:
			raise ValueError("min_samples_split must be at least 2")
		self.max_depth = max_depth
		self.min_samples_split = min_samples_split
		self.root = None

	@staticmethod
	def _entropy(labels):
		counts = Counter(labels)
		total = len(labels)
		return -sum((count / total) * log2(count / total)
					for count in counts.values())

	@staticmethod
	def _majority(labels):
		return Counter(labels).most_common(1)[0][0]

	def _best_split(self, rows, labels):
		parent_entropy = self._entropy(labels)
		best_gain, best_feature, best_threshold = 0, None, None

		for feature in range(len(rows[0])):
			values = sorted({row[feature] for row in rows})
			for a, b in zip(values, values[1:]):
				threshold = (a + b) / 2
				left = [i for i, row in enumerate(rows)
						if row[feature] <= threshold]
				right = [i for i, row in enumerate(rows)
						 if row[feature] > threshold]
				if not left or not right:
					continue
				weighted = (len(left) * self._entropy([labels[i] for i in left]) +
							len(right) * self._entropy([labels[i] for i in right])) / len(labels)
				gain = parent_entropy - weighted
				if gain > best_gain:
					best_gain, best_feature, best_threshold = gain, feature, threshold
		return best_feature, best_threshold

	def _build(self, rows, labels, depth):
		prediction = self._majority(labels)
		if (len(set(labels)) == 1 or len(rows) < self.min_samples_split or
				(self.max_depth is not None and depth >= self.max_depth)):
			return _Node(prediction=prediction)

		feature, threshold = self._best_split(rows, labels)
		if feature is None:
			return _Node(prediction=prediction)
		left_rows, left_labels, right_rows, right_labels = [], [], [], []
		for row, label in zip(rows, labels):
			target = (left_rows, left_labels) if row[feature] <= threshold else (right_rows, right_labels)
			target[0].append(row)
			target[1].append(label)
		return _Node(feature=feature, threshold=threshold,
					 left=self._build(left_rows, left_labels, depth + 1),
					 right=self._build(right_rows, right_labels, depth + 1))

	def fit(self, X, y):
		if not X or len(X) != len(y):
			raise ValueError("X and y must be non-empty and have equal lengths")
		if any(len(row) != len(X[0]) for row in X):
			raise ValueError("all rows in X must have the same length")
		self.root = self._build(X, list(y), 0)
		return self

	def _predict_one(self, row):
		node = self.root
		while node.feature is not None:
			node = node.left if row[node.feature] <= node.threshold else node.right
		return node.prediction

	def predict(self, X):
		if self.root is None:
			raise ValueError("fit the tree before predicting")
		return [self._predict_one(row) for row in X]


if __name__ == "__main__":
	tree = DecisionTree(max_depth=2).fit(
		[[0, 0], [0, 1], [1, 0], [1, 1]], ["no", "yes", "yes", "yes"])
	print(tree.predict([[0, 0], [1, 1]]))
