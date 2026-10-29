"""Find shortest paths between every pair of vertices."""


def floyd_warshall(graph):
	"""Return a matrix of all-pairs shortest-path distances.

	``graph[i][j]`` is the direct edge weight from vertex ``i`` to ``j``;
	use ``float('inf')`` when no direct edge exists. Negative edges are
	supported, but negative cycles raise ``ValueError``.
	"""
	vertex_count = len(graph)
	if any(len(row) != vertex_count for row in graph):
		raise ValueError("graph must be a square matrix")

	distances = [list(row) for row in graph]
	for vertex in range(vertex_count):
		distances[vertex][vertex] = min(distances[vertex][vertex], 0)

	for intermediate in range(vertex_count):
		for source in range(vertex_count):
			for destination in range(vertex_count):
				distances[source][destination] = min(
					distances[source][destination],
					distances[source][intermediate]
					+ distances[intermediate][destination],
				)

	if any(distances[vertex][vertex] < 0 for vertex in range(vertex_count)):
		raise ValueError("graph contains a negative-weight cycle")

	return distances


if __name__ == "__main__":
	infinity = float("inf")
	graph = [
		[0, 3, 8, infinity, -4],
		[infinity, 0, infinity, 1, 7],
		[infinity, 4, 0, infinity, infinity],
		[2, infinity, -5, 0, infinity],
		[infinity, infinity, infinity, 6, 0],
	]

	for row in floyd_warshall(graph):
		print(row)
