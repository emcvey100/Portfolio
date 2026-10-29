"""Particle Swarm Optimization.

PSO searches for the minimum of a continuous objective function.  Each
particle remembers its best position and is also guided by the swarm's best
position found so far.
"""

from __future__ import annotations

import random
from typing import Callable, Sequence


def particle_swarm_optimization(
    objective: Callable[[list[float]], float],
    bounds: Sequence[tuple[float, float]],
    *,
    particles: int = 30,
    iterations: int = 100,
    inertia: float = 0.7,
    cognitive: float = 1.5,
    social: float = 1.5,
    seed: int | None = None,
) -> tuple[list[float], float]:
    """Return the best position and value found by a particle swarm.

    ``bounds`` contains one ``(lower, upper)`` pair for each dimension.
    ``objective`` is minimized.
    """
    if not bounds:
        raise ValueError("bounds must contain at least one dimension")
    if particles < 1 or iterations < 0:
        raise ValueError("particles must be positive and iterations non-negative")
    if any(lower >= upper for lower, upper in bounds):
        raise ValueError("each lower bound must be less than its upper bound")

    rng = random.Random(seed)
    dimensions = len(bounds)
    positions = [
        [rng.uniform(lower, upper) for lower, upper in bounds]
        for _ in range(particles)
    ]
    velocities = [
        [rng.uniform(-(upper - lower), upper - lower) for lower, upper in bounds]
        for _ in range(particles)
    ]

    personal_best_positions = [position[:] for position in positions]
    personal_best_values = [objective(position) for position in positions]
    best_index = min(range(particles), key=personal_best_values.__getitem__)
    global_best_position = personal_best_positions[best_index][:]
    global_best_value = personal_best_values[best_index]

    for _ in range(iterations):
        for index in range(particles):
            for dimension, (lower, upper) in enumerate(bounds):
                r1, r2 = rng.random(), rng.random()
                velocities[index][dimension] = (
                    inertia * velocities[index][dimension]
                    + cognitive * r1 * (
                        personal_best_positions[index][dimension]
                        - positions[index][dimension]
                    )
                    + social * r2 * (
                        global_best_position[dimension]
                        - positions[index][dimension]
                    )
                )
                positions[index][dimension] = max(
                    lower,
                    min(upper, positions[index][dimension] + velocities[index][dimension]),
                )

            value = objective(positions[index])
            if value < personal_best_values[index]:
                personal_best_values[index] = value
                personal_best_positions[index] = positions[index][:]
                if value < global_best_value:
                    global_best_value = value
                    global_best_position = positions[index][:]

    return global_best_position, global_best_value


if __name__ == "__main__":
    best_position, best_value = particle_swarm_optimization(
        lambda point: sum(value * value for value in point),
        [(-10, 10), (-10, 10)],
        seed=42,
    )
    print(f"Best position: {best_position}")
    print(f"Best value: {best_value}")
