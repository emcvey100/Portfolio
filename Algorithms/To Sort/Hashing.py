"""A simple hash table implementation using separate chaining."""


class HashTable:
	"""Store key-value pairs and resolve collisions with linked buckets."""

	def __init__(self, capacity=8):
		if capacity < 1:
			raise ValueError("capacity must be positive")
		self._buckets = [[] for _ in range(capacity)]
		self._size = 0

	def _bucket(self, key):
		return self._buckets[hash(key) % len(self._buckets)]

	def put(self, key, value):
		bucket = self._bucket(key)
		for index, (stored_key, _) in enumerate(bucket):
			if stored_key == key:
				bucket[index] = (key, value)
				return

		bucket.append((key, value))
		self._size += 1
		if self._size / len(self._buckets) > 0.75:
			self._resize()

	def get(self, key, default=None):
		for stored_key, value in self._bucket(key):
			if stored_key == key:
				return value
		return default

	def remove(self, key):
		bucket = self._bucket(key)
		for index, (stored_key, value) in enumerate(bucket):
			if stored_key == key:
				del bucket[index]
				self._size -= 1
				return value
		raise KeyError(key)

	def _resize(self):
		entries = list(self.items())
		self._buckets = [[] for _ in range(len(self._buckets) * 2)]
		for key, value in entries:
			self._bucket(key).append((key, value))

	def items(self):
		for bucket in self._buckets:
			yield from bucket

	def __len__(self):
		return self._size

	def __contains__(self, key):
		return any(stored_key == key for stored_key, _ in self._bucket(key))
