"""Kohonen self-organizing map (SOM) implementation."""

from __future__ import annotations

import numpy as np


class KohonenSOM:
	"""A two-dimensional rectangular self-organizing map."""

	def __init__(self, rows: int, cols: int, input_dim: int,
				 seed: int | None = None) -> None:
		if min(rows, cols, input_dim) <= 0:
			raise ValueError("rows, cols, and input_dim must be positive")

		self.rows = rows
		self.cols = cols
		self.input_dim = input_dim
		rng = np.random.default_rng(seed)
		self.weights = rng.random((rows, cols, input_dim))
		self._locations = np.indices((rows, cols)).transpose(1, 2, 0)

	def winner(self, sample: np.ndarray) -> tuple[int, int]:
		"""Return the best matching unit (row, column) for a sample."""
		sample = np.asarray(sample, dtype=float)
		if sample.shape != (self.input_dim,):
			raise ValueError(f"sample must have shape ({self.input_dim},)")
		distances = np.sum((self.weights - sample) ** 2, axis=2)
		return tuple(np.unravel_index(np.argmin(distances), distances.shape))

	def fit(self, data: np.ndarray, epochs: int = 100,
			learning_rate: float = 0.5, radius: float | None = None,
			seed: int | None = None) -> "KohonenSOM":
		"""Train the map with online competitive learning."""
		data = np.asarray(data, dtype=float)
		if data.ndim != 2 or data.shape[1] != self.input_dim or len(data) == 0:
			raise ValueError(f"data must have shape (n, {self.input_dim})")
		if epochs <= 0 or learning_rate <= 0:
			raise ValueError("epochs and learning_rate must be positive")

		rng = np.random.default_rng(seed)
		initial_radius = radius if radius is not None else max(self.rows, self.cols) / 2
		if initial_radius <= 0:
			raise ValueError("radius must be positive")

		for epoch in range(epochs):
			progress = epoch / max(epochs - 1, 1)
			rate = learning_rate * np.exp(-progress)
			current_radius = initial_radius * np.exp(
				-progress * np.log(initial_radius + 1)
			)
			for sample in rng.permutation(data):
				row, col = self.winner(sample)
				grid_distance = np.sum(
					(self._locations - (row, col)) ** 2, axis=2
				)
				influence = np.exp(
					-grid_distance / (2 * current_radius ** 2)
				)
				self.weights += rate * influence[..., None] * (sample - self.weights)
		return self

	def transform(self, data: np.ndarray) -> np.ndarray:
		"""Return winning grid coordinates for each input vector."""
		data = np.asarray(data, dtype=float)
		if data.ndim != 2 or data.shape[1] != self.input_dim:
			raise ValueError(f"data must have shape (n, {self.input_dim})")
		return np.asarray([self.winner(sample) for sample in data], dtype=int)


if __name__ == "__main__":
	rng = np.random.default_rng(7)
	data = rng.random((200, 2))
	som = KohonenSOM(8, 8, 2, seed=7).fit(data, epochs=50, seed=7)
	print(som.transform(data[:5]))
