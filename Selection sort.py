def selection_sort(values):
    """Return a list sorted in ascending order using selection sort."""
    result = list(values)

    for i in range(len(result) - 1):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j

        if smallest != i:
            result[i], result[smallest] = result[smallest], result[i]

    return result