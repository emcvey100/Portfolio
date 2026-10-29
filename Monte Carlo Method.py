"""Estimate pi using the Monte Carlo method."""

import random


def estimate_pi(samples: int = 100_000) -> float:
    """Return an approximation of pi using randomly generated points."""
    if samples <= 0:
        raise ValueError("samples must be greater than zero")

    inside_circle = 0
    for _ in range(samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            inside_circle += 1

    return 4 * inside_circle / samples


if __name__ == "__main__":
    print(f"Estimated pi: {estimate_pi():.6f}")