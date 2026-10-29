"""A small, dependency-free Random Forest classifier."""

from collections import Counter
from math import sqrt
from random import Random


class _DecisionTree:
	def __init__(self, max_depth, min_samples_split, max_features, rng):
		self.max_depth = max_depth
		self.min_samples_split = min_samples_split
		self.max_features = max_features
		self.rng = rng
		self.root = None

	@staticmethod
	def _gini(labels):
		counts = Counter(labels)
		return 1 - sum((n / len(labels)) ** 2 for n in counts.values())

	def fit(self, rows, labels):
		self.root = self._grow(rows, labels, 0)

	def _grow(self, rows, labels, depth):
		majority = Counter(labels).most_common(1)[0][0]
		if (depth >= self.max_depth or len(set(labels)) == 1 or
				len(rows) < self.min_samples_split):
			return (majority,)

		best = None
		parent = self._gini(labels)
		features = self.rng.sample(range(len(rows[0])),
								   min(self.max_features, len(rows[0])))
		for feature in features:
			for threshold in sorted({row[feature] for row in rows})[:-1]:
				left = [i for i, row in enumerate(rows) if row[feature] <= threshold]
				right = [i for i, row in enumerate(rows) if row[feature] > threshold]
				impurity = (len(left) * self._gini([labels[i] for i in left]) +
							len(right) * self._gini([labels[i] for i in right])) / len(labels)
				candidate = (parent - impurity, feature, threshold, left, right)
				if best is None or candidate[0] > best[0]:
					best = candidate
		if best is None or best[0] <= 0:
			return (majority,)
		_, feature, threshold, left, right = best
		return (feature, threshold,
				self._grow([rows[i] for i in left], [labels[i] for i in left], depth + 1),
				self._grow([rows[i] for i in right], [labels[i] for i in right], depth + 1))

	def predict_one(self, row):
		node = self.root
		while len(node) > 1:
			node = node[2] if row[node[0]] <= node[1] else node[3]
		return node[0]


class RandomForestClassifier:
	"""An ensemble of bootstrap-sampled decision trees."""

	def __init__(self, n_trees=25, max_depth=10, min_samples_split=2,
				 max_features=None, seed=None):
		self.n_trees = n_trees
		self.max_depth = max_depth
		self.min_samples_split = min_samples_split
		self.max_features = max_features
		self.rng = Random(seed)
		self.trees = []

	def fit(self, X, y):
		if not X or len(X) != len(y):
			raise ValueError("X and y must be non-empty and have equal lengths")
		features = self.max_features or max(1, int(sqrt(len(X[0]))))
		self.trees = []
		for _ in range(self.n_trees):
			sample = [self.rng.randrange(len(X)) for _ in X]
			tree = _DecisionTree(self.max_depth, self.min_samples_split,
								 features, self.rng)
			tree.fit([X[i] for i in sample], [y[i] for i in sample])
			self.trees.append(tree)
		return self

	def predict(self, X):
		if not self.trees:
			raise ValueError("fit the classifier before predicting")
		return [Counter(tree.predict_one(row) for tree in self.trees).most_common(1)[0][0]
				for row in X]
