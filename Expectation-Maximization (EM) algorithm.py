"""Expectation-Maximization for a Gaussian mixture model.

The implementation uses only NumPy and exposes a small, sklearn-like API.
"""

from __future__ import annotations

import numpy as np


class GaussianMixtureEM:
    """Fit a mixture of multivariate Gaussian distributions with EM."""

    def __init__(self, n_components: int, max_iter: int = 100, tol: float = 1e-4,
                 random_state: int | None = None) -> None:
        if n_components < 1:
            raise ValueError("n_components must be positive")
        self.n_components = n_components
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state

    def fit(self, X: np.ndarray) -> "GaussianMixtureEM":
        """Estimate mixture parameters from rows of ``X``."""
        X = np.asarray(X, dtype=float)
        if X.ndim != 2 or len(X) < self.n_components:
            raise ValueError("X must be a 2-D array with enough samples")

        rng = np.random.default_rng(self.random_state)
        n_samples, n_features = X.shape
        indices = rng.choice(n_samples, self.n_components, replace=False)
        self.means_ = X[indices].copy()
        covariance = np.cov(X, rowvar=False) if n_features > 1 else np.array([[np.var(X)]])
        covariance = np.atleast_2d(covariance) + 1e-6 * np.eye(n_features)
        self.covariances_ = np.repeat(covariance[None, :, :], self.n_components, axis=0)
        self.weights_ = np.full(self.n_components, 1 / self.n_components)
        self.lower_bound_ = -np.inf

        for _ in range(self.max_iter):
            responsibilities, log_likelihood = self._expectation(X)
            counts = responsibilities.sum(axis=0) + 1e-12
            self.weights_ = counts / n_samples
            self.means_ = (responsibilities.T @ X) / counts[:, None]
            for component in range(self.n_components):
                centered = X - self.means_[component]
                self.covariances_[component] = (
                    (responsibilities[:, component, None] * centered).T @ centered
                    / counts[component]
                    + 1e-6 * np.eye(n_features)
                )
            if abs(log_likelihood - self.lower_bound_) < self.tol:
                break
            self.lower_bound_ = log_likelihood
        return self

    def _expectation(self, X: np.ndarray) -> tuple[np.ndarray, float]:
        log_prob = np.empty((len(X), self.n_components))
        for k, (mean, covariance) in enumerate(zip(self.means_, self.covariances_)):
            sign, logdet = np.linalg.slogdet(covariance)
            if sign <= 0:
                raise np.linalg.LinAlgError("covariance matrix is not positive definite")
            centered = X - mean
            quadratic = np.einsum("ij,jk,ik->i", centered, np.linalg.inv(covariance), centered)
            log_prob[:, k] = np.log(self.weights_[k]) - 0.5 * (
                len(mean) * np.log(2 * np.pi) + logdet + quadratic
            )
        maximum = log_prob.max(axis=1, keepdims=True)
        normalizer = maximum + np.log(np.exp(log_prob - maximum).sum(axis=1, keepdims=True))
        return np.exp(log_prob - normalizer), float(normalizer.sum())

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Return each sample's probability of belonging to every component."""
        return self._expectation(np.asarray(X, dtype=float))[0]

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Return the most likely component for each sample."""
        return self.predict_proba(X).argmax(axis=1)


if __name__ == "__main__":
    data = np.array([[1.0], [1.2], [0.8], [5.0], [5.2], [4.8]])
    model = GaussianMixtureEM(n_components=2, random_state=0).fit(data)
    print(model.predict(data))