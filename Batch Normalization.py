"""Batch normalization for dense-layer activations."""

import numpy as np


class BatchNormalization:
	"""Normalize features across a mini-batch during training and inference."""

	def __init__(self, features, momentum=0.9, epsilon=1e-5):
		if features <= 0:
			raise ValueError("features must be positive")
		self.momentum = momentum
		self.epsilon = epsilon
		self.gamma = np.ones(features)
		self.beta = np.zeros(features)
		self.running_mean = np.zeros(features)
		self.running_variance = np.ones(features)
		self._cache = None

	def forward(self, x, training=True):
		"""Return normalized activations for a 2-D batch."""
		x = np.asarray(x, dtype=float)
		if x.ndim != 2 or x.shape[1] != self.gamma.size:
			raise ValueError("x must have shape (batch_size, features)")

		if training:
			mean = x.mean(axis=0)
			variance = x.var(axis=0)
			inverse_std = 1.0 / np.sqrt(variance + self.epsilon)
			normalized = (x - mean) * inverse_std
			self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * mean
			self.running_variance = (
				self.momentum * self.running_variance
				+ (1 - self.momentum) * variance
			)
			self._cache = normalized, inverse_std
		else:
			normalized = (x - self.running_mean) / np.sqrt(
				self.running_variance + self.epsilon
			)
		return self.gamma * normalized + self.beta

	def backward(self, gradient):
		"""Return the input gradient and store parameter gradients."""
		if self._cache is None:
			raise RuntimeError("call forward with training=True first")
		normalized, inverse_std = self._cache
		gradient = np.asarray(gradient, dtype=float)
		if gradient.shape != normalized.shape:
			raise ValueError("gradient must match the input shape")

		batch_size = gradient.shape[0]
		self.gamma_gradient = np.sum(gradient * normalized, axis=0)
		self.beta_gradient = np.sum(gradient, axis=0)
		scaled = gradient * self.gamma
		return inverse_std / batch_size * (
			batch_size * scaled
			- scaled.sum(axis=0)
			- normalized * np.sum(scaled * normalized, axis=0)
		)
