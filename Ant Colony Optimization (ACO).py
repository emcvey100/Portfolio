"""Ant Colony Optimization (ACO) for the travelling salesperson problem."""

from __future__ import annotations

import random
from math import hypot
from typing import Sequence


def ant_colony_optimization(
	cities: Sequence[tuple[float, float]],
	ants: int = 20,
	iterations: int = 100,
	alpha: float = 1.0,
	beta: float = 3.0,
	evaporation: float = 0.5,
	q: float = 100.0,
	seed: int | None = None,
) -> tuple[list[int], float]:
	"""Return a short tour and its length for a set of 2D city coordinates."""
	if len(cities) < 2:
		raise ValueError("At least two cities are required")
	if ants < 1 or iterations < 1 or not 0 < evaporation <= 1:
		raise ValueError("ants and iterations must be positive; evaporation must be in (0, 1]")

	rng = random.Random(seed)
	count = len(cities)
	distances = [[0.0] * count for _ in range(count)]
	for i in range(count):
		for j in range(i + 1, count):
			distance = hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])
			distances[i][j] = distances[j][i] = distance

	pheromone = [[1.0] * count for _ in range(count)]

	def tour_length(tour: list[int]) -> float:
		return sum(distances[tour[i]][tour[(i + 1) % count]] for i in range(count))

	best_tour: list[int] = []
	best_length = float("inf")
	for _ in range(iterations):
		tours: list[tuple[list[int], float]] = []
		for _ in range(ants):
			tour = [rng.randrange(count)]
			unvisited = set(range(count)) - set(tour)
			while unvisited:
				current = tour[-1]
				choices = list(unvisited)
				weights = [
					pheromone[current][city] ** alpha
					* (1 / max(distances[current][city], 1e-12)) ** beta
					for city in choices
				]
				next_city = rng.choices(choices, weights=weights)[0]
				tour.append(next_city)
				unvisited.remove(next_city)
			length = tour_length(tour)
			tours.append((tour, length))
			if length < best_length:
				best_tour, best_length = tour[:], length

		for row in pheromone:
			for city in range(count):
				row[city] *= 1 - evaporation
		for tour, length in tours:
			deposit = q / max(length, 1e-12)
			for i, city in enumerate(tour):
				next_city = tour[(i + 1) % count]
				pheromone[city][next_city] += deposit
				pheromone[next_city][city] += deposit

	return best_tour, best_length


if __name__ == "__main__":
	cities = [(0, 0), (2, 6), (5, 3), (8, 7), (7, 1)]
	tour, length = ant_colony_optimization(cities, seed=42)
	print("Best tour:", tour)
	print(f"Tour length: {length:.2f}")
