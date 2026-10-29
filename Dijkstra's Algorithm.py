"""Dijkstra's shortest-path algorithm.

The graph is represented as {vertex: [(neighbour, edge_weight), ...]}.
"""

from heapq import heappop, heappush


def dijkstra(graph, start):
	"""Return the shortest distances and predecessor map from ``start``.

	All edge weights must be non-negative.
	"""
	distances = {vertex: float("inf") for vertex in graph}
	previous = {vertex: None for vertex in graph}
	distances[start] = 0
	queue = [(0, start)]

	while queue:
		distance, vertex = heappop(queue)
		if distance != distances[vertex]:
			continue

		for neighbour, weight in graph.get(vertex, []):
			if weight < 0:
				raise ValueError("Dijkstra's algorithm requires non-negative weights")
			new_distance = distance + weight
			if new_distance < distances.get(neighbour, float("inf")):
				distances[neighbour] = new_distance
				previous[neighbour] = vertex
				heappush(queue, (new_distance, neighbour))

	return distances, previous


def shortest_path(graph, start, end):
	"""Return the shortest path from ``start`` to ``end`` and its distance."""
	distances, previous = dijkstra(graph, start)
	if distances.get(end, float("inf")) == float("inf"):
		return [], float("inf")

	path = []
	vertex = end
	while vertex is not None:
		path.append(vertex)
		vertex = previous[vertex]
	path.reverse()
	return path, distances[end]


if __name__ == "__main__":
	graph = {
		"A": [("B", 4), ("C", 1)],
		"B": [("D", 1)],
		"C": [("B", 2), ("D", 5)],
		"D": [],
	}
	print(shortest_path(graph, "A", "D"))  # (['A', 'C', 'B', 'D'], 4)
