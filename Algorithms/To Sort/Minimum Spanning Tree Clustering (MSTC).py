"""Minimum Spanning Tree Clustering.

Clusters are formed by building a minimum spanning tree of the complete
graph, then removing its largest edges until the requested number of
clusters remains.
"""

from math import dist
from typing import Callable, Hashable, Sequence


def minimum_spanning_tree_clustering(
	points: Sequence[Sequence[float]],
	n_clusters: int,
	distance: Callable[[Sequence[float], Sequence[float]], float] = dist,
) -> list[int]:
	"""Return a cluster label for every point using MST clustering.

	``n_clusters`` must be between one and the number of points.  Euclidean
	distance is used by default; a custom distance function can be supplied.
	"""
	n = len(points)
	if n == 0:
		if n_clusters != 0:
			raise ValueError("n_clusters must be zero for empty input")
		return []
	if not 1 <= n_clusters <= n:
		raise ValueError("n_clusters must be between 1 and len(points)")

	# Kruskal's algorithm constructs the MST.
	edges = sorted(
		(distance(points[i], points[j]), i, j)
		for i in range(n)
		for j in range(i + 1, n)
	)
	parent = list(range(n))
	size = [1] * n

	def find(vertex: int) -> int:
		while parent[vertex] != vertex:
			parent[vertex] = parent[parent[vertex]]
			vertex = parent[vertex]
		return vertex

	def union(left: int, right: int) -> bool:
		left, right = find(left), find(right)
		if left == right:
			return False
		if size[left] < size[right]:
			left, right = right, left
		parent[right] = left
		size[left] += size[right]
		return True

	tree_edges: list[tuple[float, int, int]] = []
	for edge in edges:
		if union(edge[1], edge[2]):
			tree_edges.append(edge)
			if len(tree_edges) == n - 1:
				break

	# Keep the smallest n - n_clusters MST edges, removing the longest ones.
	for _, left, right in sorted(tree_edges)[: n - n_clusters]:
		union(left, right)

	labels: dict[int, int] = {}
	result: list[int] = []
	for vertex in range(n):
		root = find(vertex)
		if root not in labels:
			labels[root] = len(labels)
		result.append(labels[root])
	return result


if __name__ == "__main__":
	sample = [(1, 1), (1, 2), (2, 1), (8, 8), (9, 8)]
	print(minimum_spanning_tree_clustering(sample, 2))
