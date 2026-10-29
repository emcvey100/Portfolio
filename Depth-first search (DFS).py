"""Depth-first search (DFS) for a graph."""


def depth_first_search(graph, start):
	"""Return vertices visited from ``start`` using recursive DFS."""
	visited = set()
	order = []

	def visit(vertex):
		if vertex in visited:
			return

		visited.add(vertex)
		order.append(vertex)
		for neighbour in graph.get(vertex, []):
			visit(neighbour)

	visit(start)
	return order


def depth_first_search_iterative(graph, start):
	"""Return vertices visited from ``start`` using an explicit stack."""
	visited = set()
	order = []
	stack = [start]

	while stack:
		vertex = stack.pop()
		if vertex in visited:
			continue

		visited.add(vertex)
		order.append(vertex)
		# Reverse neighbours so traversal follows the graph's listed order.
		stack.extend(reversed(graph.get(vertex, [])))

	return order


if __name__ == "__main__":
	graph = {
		"A": ["B", "C"],
		"B": ["D", "E"],
		"C": ["F"],
		"D": [],
		"E": [],
		"F": [],
	}
	print(depth_first_search(graph, "A"))
