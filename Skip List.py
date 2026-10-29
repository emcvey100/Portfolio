"""A probabilistic ordered set implemented with a skip list."""

from random import random


class _Node:
	def __init__(self, key, height):
		self.key = key
		self.forward = [None] * height


class SkipList:
	"""Store comparable, unique keys with average O(log n) operations."""

	def __init__(self, max_level=16, probability=0.5):
		if max_level < 1:
			raise ValueError("max_level must be positive")
		if not 0 < probability < 1:
			raise ValueError("probability must be between 0 and 1")
		self.max_level = max_level
		self.probability = probability
		self.level = 1
		self.size = 0
		self.head = _Node(None, max_level)

	def _random_level(self):
		level = 1
		while level < self.max_level and random() < self.probability:
			level += 1
		return level

	def search(self, key):
		current = self.head
		for level in range(self.level - 1, -1, -1):
			while (current.forward[level] is not None and
				   current.forward[level].key < key):
				current = current.forward[level]
		current = current.forward[0]
		return current.key if current is not None and current.key == key else None

	def insert(self, key):
		update = [None] * self.max_level
		current = self.head
		for level in range(self.level - 1, -1, -1):
			while (current.forward[level] is not None and
				   current.forward[level].key < key):
				current = current.forward[level]
			update[level] = current

		current = current.forward[0]
		if current is not None and current.key == key:
			return False

		node_level = self._random_level()
		if node_level > self.level:
			for level in range(self.level, node_level):
				update[level] = self.head
			self.level = node_level
		node = _Node(key, node_level)
		for level in range(node_level):
			node.forward[level] = update[level].forward[level]
			update[level].forward[level] = node
		self.size += 1
		return True

	def remove(self, key):
		update = [None] * self.max_level
		current = self.head
		for level in range(self.level - 1, -1, -1):
			while (current.forward[level] is not None and
				   current.forward[level].key < key):
				current = current.forward[level]
			update[level] = current

		current = current.forward[0]
		if current is None or current.key != key:
			return False
		for level in range(self.level):
			if update[level].forward[level] is not current:
				break
			update[level].forward[level] = current.forward[level]
		while self.level > 1 and self.head.forward[self.level - 1] is None:
			self.level -= 1
		self.size -= 1
		return True

	def __contains__(self, key):
		return self.search(key) is not None

	def __len__(self):
		return self.size

	def __iter__(self):
		current = self.head.forward[0]
		while current is not None:
			yield current.key
			current = current.forward[0]
