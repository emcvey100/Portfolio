from collections import deque


def bellman_ford_spfa(graph, source):
	"""Return shortest distances from source using the SPFA algorithm.

	graph is an adjacency mapping where graph[u] contains (v, weight) pairs.
	Raises ValueError if a reachable negative-weight cycle exists.
	"""
	vertices = set(graph)
	for edges in graph.values():
		vertices.update(vertex for vertex, _ in edges)

	if source not in vertices:
		raise ValueError("source vertex is not in the graph")

	distances = {vertex: float("inf") for vertex in vertices}
	distances[source] = 0
	queue = deque([source])
	in_queue = {source}
	relaxations = {vertex: 0 for vertex in vertices}

	while queue:
		current = queue.popleft()
		in_queue.remove(current)

		for neighbor, weight in graph.get(current, ()):
			candidate = distances[current] + weight
			if candidate < distances[neighbor]:
				distances[neighbor] = candidate
				relaxations[neighbor] += 1
				if relaxations[neighbor] >= len(vertices):
					raise ValueError("graph contains a reachable negative-weight cycle")
				if neighbor not in in_queue:
					queue.append(neighbor)
					in_queue.add(neighbor)

	return distances


if __name__ == "__main__":
	graph = {
		"A": [("B", 4), ("C", 2)],
		"B": [("C", -3), ("D", 2)],
		"C": [("D", 3)],
		"D": [],
	}
	print(bellman_ford_spfa(graph, "A"))
