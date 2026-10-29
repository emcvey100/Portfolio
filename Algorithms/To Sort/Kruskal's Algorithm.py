"""Kruskal's algorithm for finding a minimum spanning tree."""


class DisjointSet:
	"""Union-find structure used to detect cycles."""

	def __init__(self, vertices):
		self.parent = {vertex: vertex for vertex in vertices}
		self.rank = {vertex: 0 for vertex in vertices}

	def find(self, vertex):
		if self.parent[vertex] != vertex:
			self.parent[vertex] = self.find(self.parent[vertex])
		return self.parent[vertex]

	def union(self, first, second):
		root_first = self.find(first)
		root_second = self.find(second)

		if root_first == root_second:
			return False

		if self.rank[root_first] < self.rank[root_second]:
			root_first, root_second = root_second, root_first
		self.parent[root_second] = root_first

		if self.rank[root_first] == self.rank[root_second]:
			self.rank[root_first] += 1
		return True


def kruskal(vertices, edges):
	"""Return the minimum spanning tree and its total weight.

	``edges`` should contain ``(weight, first_vertex, second_vertex)`` tuples.
	Raises ValueError if the graph is disconnected.
	"""
	disjoint_set = DisjointSet(vertices)
	minimum_spanning_tree = []
	total_weight = 0

	for weight, first, second in sorted(edges):
		if disjoint_set.union(first, second):
			minimum_spanning_tree.append((first, second, weight))
			total_weight += weight
			if len(minimum_spanning_tree) == len(vertices) - 1:
				break

	if len(minimum_spanning_tree) != len(vertices) - 1:
		raise ValueError("The graph is disconnected")

	return minimum_spanning_tree, total_weight


if __name__ == "__main__":
	vertices = {"A", "B", "C", "D"}
	edges = [
		(1, "A", "B"),
		(2, "B", "C"),
		(3, "A", "C"),
		(4, "C", "D"),
		(5, "B", "D"),
	]

	tree, weight = kruskal(vertices, edges)
	print("Minimum spanning tree:", tree)
	print("Total weight:", weight)
