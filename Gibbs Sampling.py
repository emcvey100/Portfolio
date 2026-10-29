"""Gibbs sampling for binary random variables."""

import random


def gibbs_sampling(conditional_probability, initial_state, iterations,
				   burn_in=0, random_state=None):
	"""Return samples generated from a binary joint distribution.

	``conditional_probability(state, index)`` returns the probability that
	``state[index]`` is 1, conditioned on the remaining variables.
	"""
	if iterations < 0 or burn_in < 0:
		raise ValueError("iterations and burn_in must be non-negative")
	if not initial_state:
		raise ValueError("initial_state must not be empty")
	if any(value not in (0, 1, False, True) for value in initial_state):
		raise ValueError("initial_state must contain only binary values")

	rng = random.Random(random_state)
	state = [int(value) for value in initial_state]
	samples = []

	for step in range(burn_in + iterations):
		for index in range(len(state)):
			probability = conditional_probability(state, index)
			if not 0 <= probability <= 1:
				raise ValueError("conditional probabilities must be in [0, 1]")
			state[index] = int(rng.random() < probability)
		if step >= burn_in:
			samples.append(state.copy())

	return samples
