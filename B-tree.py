"""A B-tree implementation supporting search, insertion, and traversal."""


class BTreeNode:
	def __init__(self, leaf=False):
		self.keys = []
		self.children = []
		self.leaf = leaf


class BTree:
	def __init__(self, minimum_degree=2):
		if minimum_degree < 2:
			raise ValueError("minimum_degree must be at least 2")
		self.t = minimum_degree
		self.root = BTreeNode(leaf=True)

	def search(self, key, node=None):
		"""Return True if key exists in the tree."""
		node = self.root if node is None else node
		index = 0
		while index < len(node.keys) and key > node.keys[index]:
			index += 1
		if index < len(node.keys) and key == node.keys[index]:
			return True
		return node.leaf or self.search(key, node.children[index])

	def insert(self, key):
		"""Insert key into the tree; duplicate keys are ignored."""
		if self.search(key):
			return
		if len(self.root.keys) == 2 * self.t - 1:
			old_root = self.root
			self.root = BTreeNode(leaf=False)
			self.root.children.append(old_root)
			self._split_child(self.root, 0)
		self._insert_non_full(self.root, key)

	def _insert_non_full(self, node, key):
		index = len(node.keys) - 1
		if node.leaf:
			node.keys.append(key)
			while index >= 0 and key < node.keys[index]:
				node.keys[index + 1] = node.keys[index]
				index -= 1
			node.keys[index + 1] = key
			return

		while index >= 0 and key < node.keys[index]:
			index -= 1
		index += 1
		if len(node.children[index].keys) == 2 * self.t - 1:
			self._split_child(node, index)
			if key > node.keys[index]:
				index += 1
		self._insert_non_full(node.children[index], key)

	def _split_child(self, parent, index):
		full = parent.children[index]
		right = BTreeNode(leaf=full.leaf)
		middle = full.keys[self.t - 1]
		right.keys = full.keys[self.t:]
		full.keys = full.keys[:self.t - 1]
		if not full.leaf:
			right.children = full.children[self.t:]
			full.children = full.children[:self.t]
		parent.children.insert(index + 1, right)
		parent.keys.insert(index, middle)

	def traverse(self):
		"""Return every key in ascending order."""
		result = []

		def visit(node):
			for index, key in enumerate(node.keys):
				if not node.leaf:
					visit(node.children[index])
				result.append(key)
			if not node.leaf:
				visit(node.children[-1])

		visit(self.root)
		return result


if __name__ == "__main__":
	tree = BTree(minimum_degree=3)
	for value in [10, 20, 5, 6, 12, 30, 7, 17]:
		tree.insert(value)
	print(tree.traverse())
