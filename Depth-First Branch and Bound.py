"""Depth-first branch-and-bound search."""


def depth_first_branch_and_bound(graph, start, goal, heuristic=None):
	"""Return ``(path, cost)`` for the least-cost path from ``start`` to ``goal``.

	``graph`` maps each node to an iterable of ``(neighbour, cost)`` pairs.
	``heuristic`` estimates the remaining cost and must be admissible for an
	optimal result.  Returns ``(None, float('inf'))`` if no path exists.
	"""
	if heuristic is None:
		heuristic = lambda _node: 0

	best_path = None
	best_cost = float("inf")

	def search(node, path, cost):
		nonlocal best_path, best_cost

		if cost + heuristic(node) >= best_cost:
			return
		if node == goal:
			best_path = path[:]
			best_cost = cost
			return

		children = sorted(
			graph.get(node, ()),
			key=lambda edge: cost + edge[1] + heuristic(edge[0]),
		)
		for neighbour, edge_cost in children:
			if edge_cost < 0:
				raise ValueError("edge costs must be non-negative")
			if neighbour not in path:
				search(neighbour, path + [neighbour], cost + edge_cost)

	search(start, [start], 0)
	return best_path, best_cost
