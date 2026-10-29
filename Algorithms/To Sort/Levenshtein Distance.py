"""Calculate the Levenshtein distance between two strings."""


def levenshtein_distance(first: str, second: str) -> int:
    """Return the minimum number of insertions, deletions, and substitutions."""
    if len(first) < len(second):
        first, second = second, first

    previous = list(range(len(second) + 1))
    for row, first_character in enumerate(first, start=1):
        current = [row]
        for column, second_character in enumerate(second, start=1):
            insertion = current[column - 1] + 1
            deletion = previous[column] + 1
            substitution = previous[column - 1] + (first_character != second_character)
            current.append(min(insertion, deletion, substitution))
        previous = current

    return previous[-1]


if __name__ == "__main__":
    print(levenshtein_distance(input("First string: "), input("Second string: ")))
