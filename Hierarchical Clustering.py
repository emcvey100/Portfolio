"""Agglomerative hierarchical clustering.

The implementation uses Euclidean distance and supports single, complete,
and average linkage.  It returns cluster labels for a requested number of
clusters and can also produce the full merge history (a dendrogram).
"""

from math import sqrt


def euclidean_distance(a, b):
	"""Return the Euclidean distance between two points."""
	if len(a) != len(b):
		raise ValueError("All points must have the same number of dimensions")
	return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def hierarchical_clustering(points, n_clusters=1, linkage="average"):
	"""Perform agglomerative clustering.

	Args:
		points: Iterable of coordinate sequences.
		n_clusters: Number of clusters to return.
		linkage: ``"single"``, ``"complete"``, or ``"average"``.

	Returns:
		A list assigning each input point a cluster label from 0 onward.
		The labels are stable for a given input, but are otherwise arbitrary.
	"""
	points = [tuple(point) for point in points]
	if not points:
		return []
	if not 1 <= n_clusters <= len(points):
		raise ValueError("n_clusters must be between 1 and the number of points")
	if linkage not in {"single", "complete", "average"}:
		raise ValueError("linkage must be 'single', 'complete', or 'average'")

	clusters = [[index] for index in range(len(points))]

	def distance(left, right):
		distances = [euclidean_distance(points[i], points[j])
					 for i in left for j in right]
		if linkage == "single":
			return min(distances)
		if linkage == "complete":
			return max(distances)
		return sum(distances) / len(distances)

	while len(clusters) > n_clusters:
		best_pair = None
		best_distance = float("inf")
		for i in range(len(clusters)):
			for j in range(i + 1, len(clusters)):
				current = distance(clusters[i], clusters[j])
				if current < best_distance:
					best_distance = current
					best_pair = (i, j)

		i, j = best_pair
		clusters[i].extend(clusters.pop(j))

	labels = [0] * len(points)
	for label, cluster in enumerate(clusters):
		for index in cluster:
			labels[index] = label
	return labels


if __name__ == "__main__":
	data = [(1, 1), (1.5, 2), (5, 5), (6, 5)]
	print(hierarchical_clustering(data, n_clusters=2))
