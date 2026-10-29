"""Fisher's linear discriminant analysis (LDA).

This implementation supports binary and multiclass classification using NumPy.
"""

import numpy as np


class FisherLDA:
	"""Linear discriminant classifier using class means and covariance matrices."""

	def __init__(self, regularization=1e-8):
		self.regularization = regularization

	def fit(self, X, y):
		X = np.asarray(X, dtype=float)
		y = np.asarray(y)
		if X.ndim != 2 or y.ndim != 1 or len(X) != len(y):
			raise ValueError("X must be 2-D and y must match its number of rows")

		self.classes_ = np.unique(y)
		if len(self.classes_) < 2:
			raise ValueError("At least two classes are required")

		n_features = X.shape[1]
		self.means_ = np.array([X[y == label].mean(axis=0) for label in self.classes_])
		covariance = np.zeros((n_features, n_features))
		for label, mean in zip(self.classes_, self.means_):
			centered = X[y == label] - mean
			covariance += centered.T @ centered
		covariance /= max(len(X) - len(self.classes_), 1)
		covariance += self.regularization * np.eye(n_features)
		self.inv_covariance_ = np.linalg.pinv(covariance)
		self.priors_ = np.array([np.mean(y == label) for label in self.classes_])
		return self

	def decision_function(self, X):
		X = np.asarray(X, dtype=float)
		if X.ndim == 1:
			X = X.reshape(1, -1)
		if not hasattr(self, "means_"):
			raise RuntimeError("Call fit before prediction")
		# Discriminant: xᵀΣ⁻¹μ - 1/2 μᵀΣ⁻¹μ + log prior.
		return X @ self.inv_covariance_ @ self.means_.T \
			- 0.5 * np.sum((self.means_ @ self.inv_covariance_) * self.means_, axis=1) \
			+ np.log(self.priors_)

	def predict(self, X):
		scores = self.decision_function(X)
		return self.classes_[np.argmax(scores, axis=1)]


def fisher_lda(X, y, samples):
	"""Fit Fisher LDA on ``X, y`` and return predictions for ``samples``."""
	return FisherLDA().fit(X, y).predict(samples)


if __name__ == "__main__":
	X = np.array([[1, 2], [2, 1], [2, 3], [7, 8], [8, 7], [9, 9]])
	y = np.array([0, 0, 0, 1, 1, 1])
	print(FisherLDA().fit(X, y).predict([[3, 3], [8, 8]]))
