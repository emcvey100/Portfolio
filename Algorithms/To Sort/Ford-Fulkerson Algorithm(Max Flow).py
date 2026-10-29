"""Ford-Fulkerson algorithm for finding the maximum flow in a directed graph."""


from collections import deque


def ford_fulkerson(capacity, source, sink):
	"""Return the maximum flow from ``source`` to ``sink``.

	``capacity`` is a square matrix where capacity[u][v] is the capacity of
	the edge from vertex u to vertex v.
	"""
	if not capacity or any(len(row) != len(capacity) for row in capacity):
		raise ValueError("capacity must be a non-empty square matrix")
	if not 0 <= source < len(capacity) or not 0 <= sink < len(capacity):
		raise ValueError("source and sink must be valid vertex indices")
	if source == sink:
		return 0

	residual = [row[:] for row in capacity]
	maximum_flow = 0

	while True:
		parent = [-1] * len(capacity)
		parent[source] = source
		queue = deque([source])

		while queue and parent[sink] == -1:
			vertex = queue.popleft()
			for neighbour, remaining in enumerate(residual[vertex]):
				if parent[neighbour] == -1 and remaining > 0:
					parent[neighbour] = vertex
					queue.append(neighbour)
					if neighbour == sink:
						break

		if parent[sink] == -1:
			break

		path_flow = float("inf")
		vertex = sink
		while vertex != source:
			previous = parent[vertex]
			path_flow = min(path_flow, residual[previous][vertex])
			vertex = previous

		vertex = sink
		while vertex != source:
			previous = parent[vertex]
			residual[previous][vertex] -= path_flow
			residual[vertex][previous] += path_flow
			vertex = previous

		maximum_flow += path_flow

	return maximum_flow


if __name__ == "__main__":
	graph = [
		[0, 16, 13, 0, 0, 0],
		[0, 0, 10, 12, 0, 0],
		[0, 4, 0, 0, 14, 0],
		[0, 0, 9, 0, 0, 20],
		[0, 0, 0, 7, 0, 4],
		[0, 0, 0, 0, 0, 0],
	]
	print(ford_fulkerson(graph, 0, 5))  # 23
