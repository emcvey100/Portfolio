"""A simple PageRank implementation."""


def page_rank(graph, damping=0.85, tolerance=1e-8, max_iterations=100):
	"""Return PageRank scores for a graph represented by adjacency lists."""
	if not 0 <= damping <= 1:
		raise ValueError("damping must be between 0 and 1")
	if tolerance < 0 or max_iterations < 1:
		raise ValueError("tolerance must be non-negative and max_iterations positive")

	nodes = set(graph)
	for targets in graph.values():
		nodes.update(targets)
	if not nodes:
		return {}

	nodes = tuple(nodes)
	count = len(nodes)
	links = {
		node: set(graph.get(node, ())) & set(nodes)
		for node in nodes
	}
	ranks = {node: 1 / count for node in nodes}

	for _ in range(max_iterations):
		next_ranks = {
			node: (1 - damping) / count
			for node in nodes
		}
		dangling = sum(ranks[node] for node in nodes if not links[node])
		dangling_share = damping * dangling / count
		for node in nodes:
			next_ranks[node] += dangling_share

		for source in nodes:
			if links[source]:
				share = damping * ranks[source] / len(links[source])
				for target in links[source]:
					next_ranks[target] += share

		if sum(abs(next_ranks[node] - ranks[node]) for node in nodes) < tolerance:
			ranks = next_ranks
			break
		ranks = next_ranks

	return ranks


if __name__ == "__main__":
	graph = {"A": ["B"], "B": ["A", "C"], "C": ["A"]}
	print(page_rank(graph))
