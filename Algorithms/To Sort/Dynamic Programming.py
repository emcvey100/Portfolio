"""Common dynamic-programming examples.

Dynamic programming stores solutions to overlapping subproblems so each one
is solved only once.
"""


def fibonacci(n: int) -> int:
	"""Return the nth Fibonacci number in O(n) time and O(1) space."""
	if n < 0:
		raise ValueError("n must be non-negative")

	previous, current = 0, 1
	for _ in range(n):
		previous, current = current, previous + current
	return previous


def climbing_stairs(n: int) -> int:
	"""Count ways to climb n stairs, taking one or two steps at a time."""
	if n < 0:
		return 0

	ways_to_two_back, ways_to_one_back = 1, 1
	for _ in range(n):
		ways_to_two_back, ways_to_one_back = (
			ways_to_one_back,
			ways_to_two_back + ways_to_one_back,
		)
	return ways_to_two_back


def coin_change(coins: list[int], amount: int) -> int:
	"""Return the fewest coins needed to make amount, or -1 if impossible."""
	if amount < 0:
		return -1

	impossible = amount + 1
	minimum = [0] + [impossible] * amount
	for total in range(1, amount + 1):
		for coin in coins:
			if coin > 0 and coin <= total:
				minimum[total] = min(minimum[total], minimum[total - coin] + 1)
	return -1 if minimum[amount] == impossible else minimum[amount]


if __name__ == "__main__":
	print(fibonacci(10))
	print(climbing_stairs(5))
	print(coin_change([1, 2, 5], 11))
