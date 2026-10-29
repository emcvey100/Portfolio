"""A small Gaussian Mixture Model implementation using the EM algorithm."""

import numpy as np


class GaussianMixture:
	"""Fit a mixture of multivariate normal distributions with EM."""

	def __init__(self, n_components=2, max_iter=100, tol=1e-4, random_state=None):
		if n_components < 1:
			raise ValueError("n_components must be positive")
		self.n_components = n_components
		self.max_iter = max_iter
		self.tol = tol
		self.random_state = random_state

	def fit(self, X):
		X = np.asarray(X, dtype=float)
		if X.ndim != 2 or len(X) < self.n_components:
			raise ValueError("X must contain enough rows of feature vectors")

		rng = np.random.default_rng(self.random_state)
		n_samples, n_features = X.shape
		self.means_ = X[rng.choice(n_samples, self.n_components, replace=False)].copy()
		variance = np.var(X, axis=0).mean() + 1e-6
		self.covariances_ = np.tile(np.eye(n_features) * variance,
									(self.n_components, 1, 1))
		self.weights_ = np.full(self.n_components, 1 / self.n_components)
		self.lower_bound_ = -np.inf

		for _ in range(self.max_iter):
			log_prob = self._log_gaussian(X)
			log_weighted = log_prob + np.log(self.weights_)
			log_norm = _logsumexp(log_weighted, axis=1)
			responsibilities = np.exp(log_weighted - log_norm[:, None])
			new_lower_bound = np.mean(log_norm)

			counts = responsibilities.sum(axis=0) + 1e-12
			self.weights_ = counts / n_samples
			self.means_ = (responsibilities.T @ X) / counts[:, None]
			for k in range(self.n_components):
				centered = X - self.means_[k]
				self.covariances_[k] = (
					(centered * responsibilities[:, k, None]).T @ centered / counts[k]
					+ np.eye(n_features) * 1e-6
				)
			if abs(new_lower_bound - self.lower_bound_) < self.tol:
				break
			self.lower_bound_ = new_lower_bound
		return self

	def _log_gaussian(self, X):
		values = []
		for mean, covariance in zip(self.means_, self.covariances_):
			sign, log_det = np.linalg.slogdet(covariance)
			if sign <= 0:
				raise np.linalg.LinAlgError("covariance matrix is not positive definite")
			delta = X - mean
			solved = np.linalg.solve(covariance, delta.T).T
			values.append(-0.5 * (delta * solved).sum(axis=1)
						  - 0.5 * (len(mean) * np.log(2 * np.pi) + log_det))
		return np.column_stack(values)

	def predict_proba(self, X):
		X = np.asarray(X, dtype=float)
		log_weighted = self._log_gaussian(X) + np.log(self.weights_)
		return np.exp(log_weighted - _logsumexp(log_weighted, axis=1)[:, None])

	def predict(self, X):
		return np.argmax(self.predict_proba(X), axis=1)


def _logsumexp(values, axis=None):
	maximum = np.max(values, axis=axis, keepdims=True)
	result = maximum + np.log(np.sum(np.exp(values - maximum), axis=axis, keepdims=True))
	return np.squeeze(result, axis=axis)
