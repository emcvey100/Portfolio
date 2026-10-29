"""A simple Metropolis-Hastings sampler.

The target distribution is supplied as an unnormalised density function.
"""

from math import exp, isfinite
from random import Random
from typing import Callable, List, Optional


def metropolis_hastings(
	target_density: Callable[[float], float],
	*,
	initial: float = 0.0,
	samples: int = 10_000,
	burn_in: int = 1_000,
	proposal_std: float = 1.0,
	seed: Optional[int] = None,
) -> List[float]:
	"""Draw samples using a Gaussian random-walk proposal.

	``target_density`` need not be normalised. Values returned by it must be
	non-negative and finite.
	"""
	if samples < 1 or burn_in < 0 or proposal_std <= 0:
		raise ValueError("samples must be positive, burn_in non-negative, and proposal_std positive")

	rng = Random(seed)
	current = initial
	current_density = target_density(current)
	if current_density < 0 or not isfinite(current_density):
		raise ValueError("target_density(initial) must be finite and non-negative")

	result: List[float] = []
	for step in range(samples + burn_in):
		proposal = rng.gauss(current, proposal_std)
		proposal_density = target_density(proposal)
		if proposal_density < 0 or not isfinite(proposal_density):
			raise ValueError("target_density must return finite, non-negative values")

		acceptance_ratio = (
			1.0 if current_density == 0 and proposal_density > 0
			else proposal_density / current_density if current_density else 0.0
		)
		if rng.random() < min(1.0, acceptance_ratio):
			current, current_density = proposal, proposal_density

		if step >= burn_in:
			result.append(current)
	return result


if __name__ == "__main__":
	# Standard normal density, shown without its normalising constant.
	chain = metropolis_hastings(lambda x: exp(-0.5 * x * x), seed=42)
	print(f"mean: {sum(chain) / len(chain):.3f}")
