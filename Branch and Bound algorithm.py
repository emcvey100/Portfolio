"""Branch and Bound solution for the 0/1 knapsack problem."""

from dataclasses import dataclass


@dataclass
class Item:
	value: int
	weight: int


def knapsack_branch_and_bound(
	values: list[int], weights: list[int], capacity: int
) -> tuple[int, list[int]]:
	"""Return the maximum value and selected item indices.

	The upper bound assumes that the remaining capacity may be filled
	fractionally, allowing unpromising branches to be discarded safely.
	"""
	if len(values) != len(weights):
		raise ValueError("values and weights must have the same length")
	if capacity < 0 or any(weight <= 0 for weight in weights):
		raise ValueError("capacity must be non-negative and weights positive")

	items = sorted(
		(Item(value, weight), index)
		for index, (value, weight) in enumerate(zip(values, weights))
	)
	items.sort(key=lambda pair: pair[0].value / pair[0].weight, reverse=True)

	best_value = 0
	best_indices: list[int] = []

	def bound(level: int, current_weight: int, current_value: int) -> float:
		if current_weight >= capacity:
			return float(current_value)

		estimate = float(current_value)
		remaining = capacity - current_weight
		for item, _ in items[level:]:
			if item.weight <= remaining:
				remaining -= item.weight
				estimate += item.value
			else:
				estimate += item.value * remaining / item.weight
				break
		return estimate

	def search(level: int, current_weight: int, current_value: int, chosen: list[int]) -> None:
		nonlocal best_value, best_indices
		if current_value > best_value:
			best_value = current_value
			best_indices = chosen.copy()
		if level == len(items) or bound(level, current_weight, current_value) <= best_value:
			return

		item, original_index = items[level]
		if current_weight + item.weight <= capacity:
			chosen.append(original_index)
			search(level + 1, current_weight + item.weight, current_value + item.value, chosen)
			chosen.pop()
		search(level + 1, current_weight, current_value, chosen)

	search(0, 0, 0, [])
	return best_value, sorted(best_indices)


if __name__ == "__main__":
	values = [60, 100, 120]
	weights = [10, 20, 30]
	value, selected = knapsack_branch_and_bound(values, weights, 50)
	print(f"Maximum value: {value}")
	print(f"Selected item indices: {selected}")
