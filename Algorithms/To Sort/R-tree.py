"""A compact R-tree for axis-aligned rectangles."""

from dataclasses import dataclass, field
from math import hypot
from typing import Any, List, Optional, Tuple

Rect = Tuple[float, float, float, float]


def _area(r: Rect) -> float:
	return (r[2] - r[0]) * (r[3] - r[1])


def _combine(a: Rect, b: Rect) -> Rect:
	return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


def _bounds(items) -> Rect:
	iterator = iter(items)
	result = next(iterator)
	for item in iterator:
		result = _combine(result, item)
	return result


def _overlaps(a: Rect, b: Rect) -> bool:
	return a[0] <= b[2] and b[0] <= a[2] and a[1] <= b[3] and b[1] <= a[3]


def _distance(point, rect: Rect) -> float:
	x, y = point
	return hypot(max(rect[0] - x, 0, x - rect[2]), max(rect[1] - y, 0, y - rect[3]))


@dataclass
class _Node:
	leaf: bool
	entries: list = field(default_factory=list)
	parent: Optional["_Node"] = None

	@property
	def bounds(self) -> Rect:
		return _bounds(entry[0] for entry in self.entries)


class RTree:
	"""Store rectangles and values, with insertion and spatial queries."""

	def __init__(self, max_entries: int = 8):
		if max_entries < 2:
			raise ValueError("max_entries must be at least 2")
		self.max_entries = max_entries
		self.root = _Node(True)

	def insert(self, rect: Rect, value: Any = None) -> None:
		rect = self._validate(rect)
		node = self._choose_leaf(self.root, rect)
		node.entries.append((rect, value))
		self._adjust(node)

	def search(self, rect: Rect) -> List[Any]:
		rect = self._validate(rect)
		result = []

		def visit(node):
			for bounds, item in node.entries:
				if _overlaps(bounds, rect):
					if node.leaf:
						result.append(item)
					else:
						visit(item)

		if self.root.entries:
			visit(self.root)
		return result

	def nearest(self, point: Tuple[float, float], count: int = 1) -> List[Any]:
		found = []

		def visit(node):
			for bounds, item in node.entries:
				if node.leaf:
					found.append((_distance(point, bounds), item))
				else:
					visit(item)

		visit(self.root)
		return [item for _, item in sorted(found)[:max(0, count)]]

	def _choose_leaf(self, node, rect):
		if node.leaf:
			return node
		child = min(node.entries, key=lambda e: (_area(_combine(e[0], rect)) - _area(e[0]), _area(e[0])))
		return self._choose_leaf(child[1], rect)

	def _adjust(self, node):
		while node:
			if len(node.entries) > self.max_entries:
				left, right = self._split(node)
				if node is self.root:
					self.root = _Node(False, [(left.bounds, left), (right.bounds, right)])
					left.parent = right.parent = self.root
					return
				parent = node.parent
				parent.entries = [(b, child) for b, child in parent.entries if child is not node]
				parent.entries.extend([(left.bounds, left), (right.bounds, right)])
				left.parent = right.parent = parent
				node = parent
			else:
				if node.parent:
					for i, (_, child) in enumerate(node.parent.entries):
						if child is node:
							node.parent.entries[i] = (node.bounds, node)
							break
				node = node.parent

	def _split(self, node):
		entries = sorted(node.entries, key=lambda e: (e[0][0] + e[0][2]) / 2)
		middle = len(entries) // 2
		left, right = _Node(node.leaf, entries[:middle]), _Node(node.leaf, entries[middle:])
		if not node.leaf:
			for _, child in left.entries:
				child.parent = left
			for _, child in right.entries:
				child.parent = right
		return left, right

	@staticmethod
	def _validate(rect: Rect) -> Rect:
		if len(rect) != 4 or rect[0] > rect[2] or rect[1] > rect[3]:
			raise ValueError("rect must be (min_x, min_y, max_x, max_y)")
		return tuple(float(value) for value in rect)
