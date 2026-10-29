"""A small Hopfield network for storing and recalling binary patterns.

Patterns use bipolar values: -1 and 1.  The network is trained with the
Hebbian learning rule and recalls patterns asynchronously to reduce energy.
"""

from __future__ import annotations

import random
from typing import Iterable, List, Sequence


Pattern = Sequence[int]


class HopfieldNetwork:
	"""Fully connected Hopfield network with zero-valued self-connections."""

	def __init__(self, size: int):
		if size < 1:
			raise ValueError("size must be positive")
		self.size = size
		self.weights = [[0.0] * size for _ in range(size)]

	@staticmethod
	def _validate_pattern(pattern: Pattern, size: int) -> List[int]:
		values = list(pattern)
		if len(values) != size or any(value not in (-1, 1) for value in values):
			raise ValueError(f"patterns must contain exactly {size} values of -1 or 1")
		return values

	def train(self, patterns: Iterable[Pattern]) -> None:
		"""Store patterns using the Hebbian rule."""
		patterns = [self._validate_pattern(pattern, self.size) for pattern in patterns]
		if not patterns:
			raise ValueError("at least one pattern is required")

		count = len(patterns)
		self.weights = [
			[
				0.0 if row == column else sum(pattern[row] * pattern[column] for pattern in patterns) / count
				for column in range(self.size)
			]
			for row in range(self.size)
		]

	def recall(self, pattern: Pattern, steps: int = 100, asynchronous: bool = True) -> List[int]:
		"""Recall the closest learned pattern, returning a new bipolar list."""
		state = self._validate_pattern(pattern, self.size)
		if steps < 0:
			raise ValueError("steps must not be negative")

		for _ in range(steps):
			changed = False
			indexes = list(range(self.size))
			if asynchronous:
				random.shuffle(indexes)

			for index in indexes:
				activation = sum(self.weights[index][j] * state[j] for j in range(self.size))
				new_value = 1 if activation >= 0 else -1
				if new_value != state[index]:
					state[index] = new_value
					changed = True
			if not changed:
				break
		return state

	def energy(self, pattern: Pattern) -> float:
		"""Return the network energy of a state."""
		state = self._validate_pattern(pattern, self.size)
		return -0.5 * sum(
			self.weights[i][j] * state[i] * state[j]
			for i in range(self.size)
			for j in range(self.size)
		)


if __name__ == "__main__":
	network = HopfieldNetwork(6)
	network.train([[1, 1, 1, -1, -1, -1], [-1, -1, -1, 1, 1, 1]])
	noisy = [1, 1, -1, -1, -1, -1]
	print("Input:  ", noisy)
	print("Output: ", network.recall(noisy))
