class TrieNode:
	"""A node in a prefix tree."""

	def __init__(self):
		self.children = {}
		self.is_word = False


class Trie:
	"""Trie supporting insertion, lookup, prefix lookup, and deletion."""

	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		for character in word:
			node = node.children.setdefault(character, TrieNode())
		node.is_word = True

	def search(self, word):
		node = self._find_node(word)
		return node is not None and node.is_word

	def starts_with(self, prefix):
		return self._find_node(prefix) is not None

	def delete(self, word):
		"""Remove a word if present, preserving shared prefixes."""
		def remove(node, index):
			if index == len(word):
				if not node.is_word:
					return False
				node.is_word = False
				return not node.children

			character = word[index]
			child = node.children.get(character)
			if child is None or not remove(child, index + 1):
				return False

			del node.children[character]
			return not node.is_word and not node.children

		remove(self.root, 0)

	def _find_node(self, text):
		node = self.root
		for character in text:
			node = node.children.get(character)
			if node is None:
				return None
		return node
