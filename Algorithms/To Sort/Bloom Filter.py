"""A space-efficient probabilistic set using a Bloom filter."""

from hashlib import sha256
from math import ceil, log


class BloomFilter:
	"""A set-like structure that permits false positives, but no false negatives."""

	def __init__(self, capacity: int, error_rate: float = 0.01) -> None:
		if capacity <= 0:
			raise ValueError("capacity must be positive")
		if not 0 < error_rate < 1:
			raise ValueError("error_rate must be between 0 and 1")

		self.capacity = capacity
		self.error_rate = error_rate
		self._bit_count = max(1, ceil(-capacity * log(error_rate) / log(2) ** 2))
		self._hash_count = max(1, round(self._bit_count / capacity * log(2)))
		self._bits = bytearray((self._bit_count + 7) // 8)

	def _positions(self, item: object):
		digest = sha256(str(item).encode("utf-8")).digest()
		first = int.from_bytes(digest[:8], "big")
		step = int.from_bytes(digest[8:16], "big") or 1
		for index in range(self._hash_count):
			yield (first + index * step) % self._bit_count

	def add(self, item: object) -> None:
		"""Add an item to the filter."""
		for position in self._positions(item):
			self._bits[position // 8] |= 1 << (position % 8)

	def might_contain(self, item: object) -> bool:
		"""Return False if absent; True means the item may be present."""
		return all(
			self._bits[position // 8] & (1 << (position % 8))
			for position in self._positions(item)
		)

	def __contains__(self, item: object) -> bool:
		return self.might_contain(item)
