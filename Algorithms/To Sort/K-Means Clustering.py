"""A dependency-free implementation of the k-means clustering algorithm."""

from math import dist
from random import Random
from typing import Iterable, List, Sequence, Tuple


Point = Sequence[float]


def k_means(
	points: Iterable[Point],
	k: int,
	max_iterations: int = 100,
	seed: int | None = None,
) -> Tuple[List[List[float]], List[int]]:
	"""Return ``(centres, labels)`` for the supplied points."""
	data = [list(map(float, point)) for point in points]
	if not data:
		raise ValueError("points must not be empty")
	if not 1 <= k <= len(data):
		raise ValueError("k must be between 1 and the number of points")
	if max_iterations < 1:
		raise ValueError("max_iterations must be positive")

	dimensions = len(data[0])
	if dimensions == 0 or any(len(point) != dimensions for point in data):
		raise ValueError("all points must have the same non-zero dimension")

	rng = Random(seed)
	centres = [data[index][:] for index in rng.sample(range(len(data)), k)]
	labels = [-1] * len(data)

	for _ in range(max_iterations):
		new_labels = [
			min(range(k), key=lambda cluster: dist(point, centres[cluster]))
			for point in data
		]
		new_centres = []
		for cluster in range(k):
			members = [point for point, label in zip(data, new_labels) if label == cluster]
			if members:
				new_centres.append([
					sum(point[index] for point in members) / len(members)
					for index in range(dimensions)
				])
			else:
				# Re-seed an empty cluster with the point furthest from its centre.
				index = max(
					range(len(data)),
					key=lambda i: dist(data[i], centres[new_labels[i]]),
				)
				new_centres.append(data[index][:])

		if new_labels == labels and new_centres == centres:
			break
		labels, centres = new_labels, new_centres

	return centres, labels


if __name__ == "__main__":
	sample = [(1, 1), (1.5, 2), (2, 1), (8, 8), (9, 8), (8, 9)]
	centres, labels = k_means(sample, k=2, seed=42)
	print("Centres:", centres)
	print("Clusters:", labels)
