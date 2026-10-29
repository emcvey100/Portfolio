"""A dynamic-programming solution to the 0/1 knapsack problem."""


def knapsack(weights: list[int], values: list[int], capacity: int) -> tuple[int, list[int]]:
	"""Return the maximum value and selected item indexes.

	Every item may be selected at most once.
	"""
	if len(weights) != len(values):
		raise ValueError("weights and values must have the same length")
	if capacity < 0 or any(weight < 0 for weight in weights):
		raise ValueError("capacity and weights must be non-negative")

	item_count = len(weights)
	table = [[0] * (capacity + 1) for _ in range(item_count + 1)]

	for item in range(1, item_count + 1):
		weight = weights[item - 1]
		value = values[item - 1]
		for remaining in range(capacity + 1):
			table[item][remaining] = table[item - 1][remaining]
			if weight <= remaining:
				table[item][remaining] = max(
					table[item][remaining],
					table[item - 1][remaining - weight] + value,
				)

	selected = []
	remaining = capacity
	for item in range(item_count, 0, -1):
		if table[item][remaining] != table[item - 1][remaining]:
			selected.append(item - 1)
			remaining -= weights[item - 1]

	selected.reverse()
	return table[item_count][capacity], selected


if __name__ == "__main__":
	maximum_value, selected_items = knapsack(
		weights=[2, 3, 4, 5],
		values=[3, 4, 5, 6],
		capacity=5,
	)
	print(f"Maximum value: {maximum_value}")
	print(f"Selected item indexes: {selected_items}")
