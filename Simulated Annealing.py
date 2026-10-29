"""Simulated annealing for minimising a function."""

from __future__ import annotations

import math
import random
from collections.abc import Callable, Sequence


def simulated_annealing(
	objective: Callable[[list[float]], float],
	initial: Sequence[float],
	bounds: Sequence[tuple[float, float]],
	*,
	initial_temperature: float = 100.0,
	cooling_rate: float = 0.995,
	minimum_temperature: float = 1e-8,
	iterations: int = 10_000,
	step_size: float = 1.0,
	seed: int | None = None,
) -> tuple[list[float], float]:
	"""Return the best point found while minimising ``objective``."""
	if len(initial) != len(bounds):
		raise ValueError("initial and bounds must have the same length")
	if initial_temperature <= 0 or not 0 < cooling_rate < 1:
		raise ValueError("invalid temperature settings")
	if iterations < 1 or step_size <= 0:
		raise ValueError("iterations and step_size must be positive")
	if any(lower >= upper for lower, upper in bounds):
		raise ValueError("each bound must have lower < upper")

	rng = random.Random(seed)
	current = [
		min(max(value, lower), upper)
		for value, (lower, upper) in zip(initial, bounds)
	]
	current_value = objective(current)
	best, best_value = current.copy(), current_value
	temperature = initial_temperature

	for _ in range(iterations):
		candidate = [
			min(max(value + rng.uniform(-step_size, step_size), lower), upper)
			for value, (lower, upper) in zip(current, bounds)
		]
		candidate_value = objective(candidate)
		change = candidate_value - current_value

		if change < 0 or rng.random() < math.exp(-change / temperature):
			current, current_value = candidate, candidate_value
			if current_value < best_value:
				best, best_value = current.copy(), current_value

		temperature *= cooling_rate
		if temperature < minimum_temperature:
			break

	return best, best_value


if __name__ == "__main__":
	solution, value = simulated_annealing(
		lambda point: sum(coordinate**2 for coordinate in point),
		initial=[8.0, -6.0],
		bounds=[(-10.0, 10.0), (-10.0, 10.0)],
		seed=42,
	)
	print(f"best solution: {solution}\nvalue: {value:.6f}")
