"""Lloyd's algorithm (k-means clustering)."""

from random import Random
from math import dist


def lloyds_algorithm(points, k, max_iterations=100, seed=None):
	"""Cluster points into *k* groups using Lloyd's k-means algorithm.

	Returns ``(centroids, labels)`` where each label is the index of its
	nearest centroid. Points may be any iterable of numeric coordinates.
	"""
	points = [tuple(point) for point in points]
	if not points:
		raise ValueError("points must not be empty")
	if not 1 <= k <= len(points):
		raise ValueError("k must be between 1 and the number of points")
	if any(len(point) != len(points[0]) for point in points):
		raise ValueError("all points must have the same dimension")

	rng = Random(seed)
	centroids = [tuple(point) for point in rng.sample(points, k)]

	for _ in range(max_iterations):
		labels = [
			min(range(k), key=lambda index: dist(point, centroids[index]))
			for point in points
		]
		new_centroids = []
		for index in range(k):
			cluster = [point for point, label in zip(points, labels)
					   if label == index]
			# Keep the old centroid if a cluster becomes empty.
			if cluster:
				new_centroids.append(tuple(
					sum(point[dimension] for point in cluster) / len(cluster)
					for dimension in range(len(points[0]))
				))
			else:
				new_centroids.append(centroids[index])

		if new_centroids == centroids:
			break
		centroids = new_centroids

	labels = [
		min(range(k), key=lambda index: dist(point, centroids[index]))
		for point in points
	]
	return centroids, labels


if __name__ == "__main__":
	data = [(1, 1), (1, 2), (2, 1), (8, 8), (9, 8), (8, 9)]
	centroids, labels = lloyds_algorithm(data, k=2, seed=42)
	print("Centroids:", centroids)
	print("Labels:", labels)
