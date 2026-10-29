"""Heap sort implementation."""


def heap_sort(values):
	"""Return a new list containing values sorted in ascending order."""
	result = list(values)

	def sift_down(root, end):
		while True:
			child = 2 * root + 1
			if child >= end:
				return
			if child + 1 < end and result[child] < result[child + 1]:
				child += 1
			if result[root] >= result[child]:
				return
			result[root], result[child] = result[child], result[root]
			root = child

	for root in range(len(result) // 2 - 1, -1, -1):
		sift_down(root, len(result))

	for end in range(len(result) - 1, 0, -1):
		result[0], result[end] = result[end], result[0]
		sift_down(0, end)

	return result
