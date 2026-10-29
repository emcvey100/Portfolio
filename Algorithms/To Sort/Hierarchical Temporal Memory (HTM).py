"""Minimal Hierarchical Temporal Memory (HTM) demonstration.

The spatial pooler converts inputs into sparse distributed representations;
the temporal memory learns transitions between those representations.
"""

from __future__ import annotations

import random
from typing import Iterable, Sequence


class SpatialPooler:
	"""Choose the columns with the greatest overlap with a binary input."""

	def __init__(self, input_size: int, column_count: int, active_count: int,
				 seed: int | None = None) -> None:
		if not 0 < active_count <= column_count:
			raise ValueError("active_count must be between 1 and column_count")
		self.input_size = input_size
		self.active_count = active_count
		rng = random.Random(seed)
		self.synapses = [
			[rng.random() for _ in range(input_size)]
			for _ in range(column_count)
		]

	def encode(self, pattern: Sequence[int]) -> set[int]:
		if len(pattern) != self.input_size:
			raise ValueError("pattern has the wrong size")
		overlap = [
			sum(bit and weight >= 0.5 for bit, weight in zip(pattern, row))
			for row in self.synapses
		]
		ranked = sorted(range(len(overlap)),
						key=lambda column: (-overlap[column], column))
		return set(ranked[:self.active_count])


class TemporalMemory:
	"""Learn first-order transitions between active column sets."""

	def __init__(self, column_count: int, threshold: float = 0.5) -> None:
		self.threshold = threshold
		self.transitions = [[0.0] * column_count for _ in range(column_count)]
		self.previous: set[int] = set()

	def step(self, active_columns: Iterable[int]) -> set[int]:
		current = set(active_columns)
		predicted = {
			destination
			for source in self.previous
			for destination, strength in enumerate(self.transitions[source])
			if strength >= self.threshold
		}
		for source in self.previous:
			for destination in current:
				self.transitions[source][destination] = min(
					1.0, self.transitions[source][destination] + 0.25
				)
		self.previous = current
		return predicted


if __name__ == "__main__":
	pooler = SpatialPooler(input_size=8, column_count=32, active_count=4, seed=1)
	memory = TemporalMemory(column_count=32)
	sequence = (
		(1, 0, 0, 1, 0, 0, 0, 0),
		(0, 1, 0, 0, 1, 0, 0, 0),
		(0, 0, 1, 0, 0, 1, 0, 0),
	)
	for _ in range(4):
		for pattern in sequence:
			memory.step(pooler.encode(pattern))
	print("Predicted columns:", sorted(memory.step(pooler.encode(sequence[0]))))
