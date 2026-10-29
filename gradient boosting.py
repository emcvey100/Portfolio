"""Simple gradient boosting regression implementation."""


class _Tree:
	def __init__(self, depth=2, leaf_size=1):
		self.depth, self.leaf_size = depth, leaf_size
		self.node = None

	def fit(self, X, y):
		self.node = self._grow(X, y, 0)
		return self

	def _grow(self, X, y, depth):
		value = sum(y) / len(y)
		if depth >= self.depth or len(y) <= 2 * self.leaf_size:
			return (value,)
		best = None
		for column in range(len(X[0])):
			thresholds = sorted(set(row[column] for row in X))
			for threshold in thresholds[:-1]:
				left = [i for i, row in enumerate(X) if row[column] <= threshold]
				right = [i for i, row in enumerate(X) if row[column] > threshold]
				if len(left) < self.leaf_size or len(right) < self.leaf_size:
					continue
				lm = sum(y[i] for i in left) / len(left)
				rm = sum(y[i] for i in right) / len(right)
				error = sum((y[i] - lm) ** 2 for i in left)
				error += sum((y[i] - rm) ** 2 for i in right)
				if best is None or error < best[0]:
					best = error, column, threshold, left, right
		if best is None:
			return (value,)
		_, column, threshold, left, right = best
		return (column, threshold,
				self._grow([X[i] for i in left], [y[i] for i in left], depth + 1),
				self._grow([X[i] for i in right], [y[i] for i in right], depth + 1))

	def _value(self, row, node):
		if len(node) == 1:
			return node[0]
		return self._value(row, node[2] if row[node[0]] <= node[1] else node[3])

	def predict(self, X):
		return [self._value(row, self.node) for row in X]


class GradientBoostingRegressor:
	"""Gradient boosting for regression with squared-error loss."""

	def __init__(self, n_estimators=100, learning_rate=0.05, max_depth=2,
				 min_samples_leaf=1):
		self.n_estimators = n_estimators
		self.learning_rate = learning_rate
		self.max_depth = max_depth
		self.min_samples_leaf = min_samples_leaf
		self.trees = []
		self.base = None

	def fit(self, X, y):
		if not X or len(X) != len(y):
			raise ValueError("X and y must be non-empty and have equal lengths")
		self.base = sum(y) / len(y)
		prediction = [self.base] * len(y)
		self.trees = []
		for _ in range(self.n_estimators):
			residual = [actual - predicted for actual, predicted in zip(y, prediction)]
			tree = _Tree(self.max_depth, self.min_samples_leaf).fit(X, residual)
			update = tree.predict(X)
			prediction = [p + self.learning_rate * u for p, u in zip(prediction, update)]
			self.trees.append(tree)
		return self

	def predict(self, X):
		if self.base is None:
			raise RuntimeError("fit must be called before predict")
		result = [self.base] * len(X)
		for tree in self.trees:
			result = [p + self.learning_rate * u
					  for p, u in zip(result, tree.predict(X))]
		return result
