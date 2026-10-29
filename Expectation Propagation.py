"""Expectation Propagation for a one-dimensional factorised model.

EP approximates ``p(x) ∝ N(x; prior_mean, prior_variance) * ∏ f_i(x)``
with a Gaussian distribution.  Factors must be non-negative callables.
"""

from __future__ import annotations

import numpy as np


class ExpectationPropagation:
	"""Run EP using Gauss-Hermite quadrature to match tilted moments."""

	def __init__(
		self,
		factors,
		prior_mean=0.0,
		prior_variance=1.0,
		quadrature_points= 40,
	):
		if prior_variance <= 0:
			raise ValueError("prior_variance must be positive")
		if quadrature_points < 2:
			raise ValueError("quadrature_points must be at least 2")
		self.factors = list(factors)
		self.mean = float(prior_mean)
		self.variance = float(prior_variance)
		self._nodes, self._weights = np.polynomial.hermite.hermgauss(
			int(quadrature_points)
		)
		self._site_precision = np.zeros(len(self.factors))
		self._site_natural_mean = np.zeros(len(self.factors))

	def _moments(self, mean, variance, factor=None):
		x = mean + np.sqrt(2.0 * variance) * self._nodes
		weights = self._weights.copy()
		if factor is not None:
			values = np.asarray(factor(x), dtype=float)
			if values.shape == ():
				values = np.full_like(x, values)
			if values.shape != x.shape or np.any(~np.isfinite(values)) or np.any(values < 0):
				raise ValueError("factors must return finite, non-negative values")
			weights *= values
		normaliser = weights.sum()
		if normaliser <= 0:
			raise ValueError("a tilted distribution has zero mass")
		weights /= normaliser
		tilted_mean = np.dot(weights, x)
		tilted_variance = np.dot(weights, (x - tilted_mean) ** 2)
		return tilted_mean, max(float(tilted_variance), 1e-12)

	def run(self, iterations=20, tolerance=1e-8, damping=0.7):
		"""Return ``(mean, variance)`` after updating all sites."""
		if not 0 < damping <= 1:
			raise ValueError("damping must be in (0, 1]")
		prior_precision = 1.0 / self.variance
		for _ in range(iterations):
			old_mean, old_variance = self.mean, self.variance
			for i, factor in enumerate(self.factors):
				cavity_precision = prior_precision + self._site_precision.sum() - self._site_precision[i]
				cavity_natural_mean = prior_precision * self._prior_mean + self._site_natural_mean.sum() - self._site_natural_mean[i]
				cavity_variance = 1.0 / cavity_precision
				cavity_mean = cavity_natural_mean / cavity_precision
				tilted_mean, tilted_variance = self._moments(cavity_mean, cavity_variance, factor)
				new_precision = 1.0 / tilted_variance - cavity_precision
				new_natural_mean = tilted_mean / tilted_variance - cavity_precision * cavity_mean
				self._site_precision[i] = (1 - damping) * self._site_precision[i] + damping * new_precision
				self._site_natural_mean[i] = (1 - damping) * self._site_natural_mean[i] + damping * new_natural_mean
			total_precision = prior_precision + self._site_precision.sum()
			if total_precision <= 0:
				raise ValueError("EP produced an invalid Gaussian approximation")
			self.variance = 1.0 / total_precision
			self.mean = (prior_precision * self._prior_mean + self._site_natural_mean.sum()) * self.variance
			if abs(self.mean - old_mean) < tolerance and abs(self.variance - old_variance) < tolerance:
				break
		return self.mean, self.variance

	@property
	def _prior_mean(self):
		return self._stored_prior_mean

	@_prior_mean.setter
	def _prior_mean(self, value):
		self._stored_prior_mean = float(value)
