import random


def fisher_yates_shuffle(items):
    """Return a randomly shuffled copy of *items* using Fisher-Yates."""
    shuffled = list(items)

    for index in range(len(shuffled) - 1, 0, -1):
        swap_index = random.randint(0, index)
        shuffled[index], shuffled[swap_index] = (
            shuffled[swap_index],
            shuffled[index],
        )

    return shuffled