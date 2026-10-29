"""Bellman-Ford-Moore shortest-path algorithm."""


def bellman_ford(graph, source):
	"""Return shortest distances and predecessors from ``source``.

	``graph`` is a mapping of vertices to mappings of neighbours and edge
	weights. Raises ``ValueError`` when a reachable negative cycle exists.
	"""
	if source not in graph:
		raise KeyError(f"Unknown source vertex: {source!r}")

	vertices = set(graph)
	for neighbours in graph.values():
		vertices.update(neighbours)

	distance = {vertex: float("inf") for vertex in vertices}
	predecessor = {vertex: None for vertex in vertices}
	distance[source] = 0
	edges = [
		(vertex, neighbour, weight)
		for vertex, neighbours in graph.items()
		for neighbour, weight in neighbours.items()
	]

	for _ in range(max(0, len(vertices) - 1)):
		changed = False
		for vertex, neighbour, weight in edges:
			if distance[vertex] != float("inf") and (
				distance[vertex] + weight < distance[neighbour]
			):
				distance[neighbour] = distance[vertex] + weight
				predecessor[neighbour] = vertex
				changed = True
		if not changed:
			break

	for vertex, neighbour, weight in edges:
		if distance[vertex] != float("inf") and (
			distance[vertex] + weight < distance[neighbour]
		):
			raise ValueError("Graph contains a reachable negative-weight cycle")

	return distance, predecessor
