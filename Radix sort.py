"""Radix sort implementation for integers."""


def radix_sort(values: list[int]) -> list[int]:
	"""Return a sorted copy of values using least-significant-digit radix sort."""
	def sort_non_negative(items: list[int]) -> list[int]:
		result = items[:]
		place = 1
		largest = max(result, default=0)

		while largest // place:
			buckets = [[] for _ in range(10)]
			for number in result:
				buckets[(number // place) % 10].append(number)
			result = [number for bucket in buckets for number in bucket]
			place *= 10

		return result

	negatives = [-number for number in values if number < 0]
	non_negatives = [number for number in values if number >= 0]
	sorted_negatives = sort_non_negative(negatives)

	return [-number for number in reversed(sorted_negatives)] + sort_non_negative(non_negatives)


if __name__ == "__main__":
	print(radix_sort([170, 45, 75, -90, 802, 24, 2, 66]))
