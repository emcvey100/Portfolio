def linear_search(items, target):
    """Return the index of target in items, or -1 if it is not found."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1