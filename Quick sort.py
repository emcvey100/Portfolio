def quick_sort(values):
    """Return a sorted copy of values using the quick sort algorithm."""
    if len(values) <= 1:
        return list(values)

    pivot = values[len(values) // 2]
    smaller = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    larger = [value for value in values if value > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    numbers = [10, 7, 8, 9, 1, 5]
    print(quick_sort(numbers))