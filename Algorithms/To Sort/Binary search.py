def binary_search(values, target):
    """Return the index of target in sorted values, or -1 if it is absent."""
    left, right = 0, len(values) - 1

    while left <= right:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
