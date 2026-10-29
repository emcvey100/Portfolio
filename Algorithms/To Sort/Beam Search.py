"""Beam search implementation.

Beam search keeps only the best ``beam_width`` partial solutions at each
level, using less memory than breadth-first search at the cost of optimality.
"""


def beam_search(start, expand, is_goal, beam_width=3):
	"""Return a path from ``start`` to a goal, or ``None`` if none is found.

	``expand(node)`` should yield ``(next_node, step_score)`` pairs. Higher
	scores are preferred. Nodes already in the current path are ignored to
	prevent cycles.
	"""
	if beam_width < 1:
		raise ValueError("beam_width must be at least 1")

	beam = [([start], 0)]
	while beam:
		for path, total_score in beam:
			if is_goal(path[-1]):
				return path

		candidates = []
		for path, total_score in beam:
			for next_node, step_score in expand(path[-1]):
				if next_node in path:
					continue
				candidates.append(
					(path + [next_node], total_score + step_score)
				)

		candidates.sort(key=lambda item: item[1], reverse=True)
		beam = candidates[:beam_width]

	return None


if __name__ == "__main__":
	graph = {
		"A": [("B", 2), ("C", 5)],
		"B": [("D", 4)],
		"C": [("D", 1)],
		"D": [],
	}
	path = beam_search("A", graph.get, lambda node: node == "D")
	print(path)
