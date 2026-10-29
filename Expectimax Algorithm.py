"""A small, reusable implementation of the expectimax algorithm.

Expectimax alternates between maximizing decision nodes and chance nodes,
where chance outcomes are combined using their probabilities.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TypeVar


State = TypeVar("State")
Action = TypeVar("Action")


def expectimax(
    state: State,
    depth: int,
    actions: Callable[[State], Iterable[Action]],
    result: Callable[[State, Action], State],
    chance_outcomes: Callable[[State, Action], Iterable[tuple[float, State]]],
    evaluate: Callable[[State], float],
) -> tuple[Action | None, float]:
    """Return the best action and its expected value.

    ``chance_outcomes`` must yield ``(probability, next_state)`` pairs.  A
    decision chooses the action with the greatest expected value; each action
    may produce several probabilistic outcomes.
    """

    def value(current: State, remaining: int) -> float:
        if remaining == 0:
            return evaluate(current)

        choices = list(actions(current))
        if not choices:
            return evaluate(current)

        return max(
            sum(
                probability * value(next_state, remaining - 1)
                for probability, next_state in chance_outcomes(current, action)
            )
            for action in choices
        )

    choices = list(actions(state))
    if depth <= 0 or not choices:
        return None, evaluate(state)

    scored_actions = [
        (
            action,
            sum(
                probability * value(next_state, depth - 1)
                for probability, next_state in chance_outcomes(state, action)
            ),
        )
        for action in choices
    ]
    return max(scored_actions, key=lambda item: item[1])


if __name__ == "__main__":
    # A minimal example: choose between a safe reward and a risky gamble.
    actions_for = lambda state: ("safe", "gamble") if state == "start" else ()
    transitions = {
        ("start", "safe"): ((1.0, "reward 5"),),
        ("start", "gamble"): ((0.5, "reward 0"), (0.5, "reward 12")),
    }
    score = lambda state: int(state.rsplit(" ", 1)[-1]) if state.startswith("reward") else 0

    print(expectimax("start", 1, actions_for, lambda s, a: s, transitions.get, score))