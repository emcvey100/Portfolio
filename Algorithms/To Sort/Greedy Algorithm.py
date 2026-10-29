"""Greedy algorithm examples.

A greedy algorithm makes the best available local choice at each step.
The choice is never reconsidered, so this approach is efficient when the
problem has the greedy-choice property.
"""


def activity_selection(activities):
    """Return the maximum number of non-overlapping activities.

    Each activity is a ``(start, finish)`` tuple.  Activities are selected
    by earliest finishing time, which is optimal for this problem.
    """
    selected = []
    next_start = float("-inf")

    for start, finish in sorted(activities, key=lambda activity: activity[1]):
        if start >= next_start:
            selected.append((start, finish))
            next_start = finish

    return selected


def fractional_knapsack(items, capacity):
    """Return the maximum value when fractions of items may be taken.

    ``items`` contains ``(value, weight)`` pairs.  The result is the total
    value and the fraction of each item taken, in the original order.
    """
    if capacity < 0:
        raise ValueError("capacity must not be negative")

    ranked = sorted(
        enumerate(items),
        key=lambda item: item[1][0] / item[1][1],
        reverse=True,
    )
    taken = [0.0] * len(items)
    total_value = 0.0
    remaining = capacity

    for index, (value, weight) in ranked:
        if weight <= 0:
            raise ValueError("item weights must be positive")
        if remaining == 0:
            break

        fraction = min(1.0, remaining / weight)
        taken[index] = fraction
        total_value += value * fraction
        remaining -= weight * fraction

    return total_value, taken


if __name__ == "__main__":
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10)]
    print("Selected activities:", activity_selection(activities))

    items = [(60, 10), (100, 20), (120, 30)]
    print("Knapsack result:", fractional_knapsack(items, 50))
