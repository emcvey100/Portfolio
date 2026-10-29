"""Expectation-Maximization (EM) for Gaussian Mixture Models."""

import numpy as np


class GaussianMixtureEM:
	"""Fit a full-covariance Gaussian mixture using EM."""

	def __init__(self, n_components=2, max_iter=100, tol=1e-4,
				 reg_covar=1e-6, random_state=None):
		if n_components < 1:
			raise ValueError("n_components must be positive")
		self.n_components = n_components
		self.max_iter = max_iter
		self.tol = tol
		self.reg_covar = reg_covar
		self.random_state = random_state

	def fit(self, X):
		X = self._check_X(X)
		n_samples, n_features = X.shape
		rng = np.random.default_rng(self.random_state)
		self.means_ = X[rng.choice(n_samples, self.n_components,
								   replace=n_samples < self.n_components)].copy()
		covariance = np.atleast_2d(np.cov(X, rowvar=False))
		if covariance.shape != (n_features, n_features):
			covariance = np.eye(n_features)
		covariance += self.reg_covar * np.eye(n_features)
		self.covariances_ = np.repeat(covariance[None], self.n_components, axis=0)
		self.weights_ = np.full(self.n_components, 1 / self.n_components)
		old_bound = -np.inf

		for self.n_iter_ in range(1, self.max_iter + 1):
			log_joint = self._log_gaussian(X) + np.log(self.weights_)
			log_prob = self._logsumexp(log_joint, axis=1)
			responsibilities = np.exp(log_joint - log_prob[:, None])

			counts = responsibilities.sum(axis=0) + np.finfo(float).eps
			self.weights_ = counts / n_samples
			self.means_ = responsibilities.T @ X / counts[:, None]
			for k in range(self.n_components):
				centered = X - self.means_[k]
				self.covariances_[k] = (
					(responsibilities[:, k, None] * centered).T @ centered
					/ counts[k] + self.reg_covar * np.eye(n_features)
				)

			bound = float(log_prob.mean())
			if abs(bound - old_bound) < self.tol:
				break
			old_bound = bound
		self.lower_bound_ = bound
		return self

	def predict_proba(self, X):
		X = self._check_X(X)
		joint = self._log_gaussian(X) + np.log(self.weights_)
		return np.exp(joint - self._logsumexp(joint, axis=1)[:, None])

	def predict(self, X):
		return np.argmax(self.predict_proba(X), axis=1)

	def score_samples(self, X):
		X = self._check_X(X)
		return self._logsumexp(self._log_gaussian(X) + np.log(self.weights_), axis=1)

	def score(self, X):
		return float(self.score_samples(X).mean())

	def _log_gaussian(self, X):
		result = np.empty((len(X), self.n_components))
		for k, covariance in enumerate(self.covariances_):
			sign, logdet = np.linalg.slogdet(covariance)
			if sign <= 0:
				raise np.linalg.LinAlgError("covariance is not positive definite")
			centered = X - self.means_[k]
			distance = np.einsum("ij,jk,ik->i", centered,
								 np.linalg.inv(covariance), centered)
			result[:, k] = -0.5 * (X.shape[1] * np.log(2 * np.pi)
								   + logdet + distance)
		return result

	@staticmethod
	def _logsumexp(values, axis):
		maximum = np.max(values, axis=axis, keepdims=True)
		return (maximum + np.log(np.sum(np.exp(values - maximum), axis=axis,
										keepdims=True))).squeeze(axis)

	@staticmethod
	def _check_X(X):
		X = np.asarray(X, dtype=float)
		if X.ndim == 1:
			X = X[:, None]
		if X.ndim != 2 or not len(X) or not np.isfinite(X).all():
			raise ValueError("X must be a non-empty, finite 2D array")
		return X
