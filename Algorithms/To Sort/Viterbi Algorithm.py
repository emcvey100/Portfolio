"""Viterbi algorithm for finding the most likely hidden-state sequence."""


def viterbi(observations, states, start_probability, transition_probability,
			emission_probability):
	"""Return the most likely state sequence and its probability.

	``transition_probability[a][b]`` is P(state b | state a), and
	``emission_probability[state][observation]`` is P(observation | state).
	"""
	observations = list(observations)
	states = list(states)

	if not observations or not states:
		return [], 0.0

	missing = [state for state in states if state not in start_probability]
	if missing:
		raise ValueError(f"Missing start probability for: {missing[0]}")

	probabilities = {}
	backpointers = []

	first_observation = observations[0]
	probabilities = {
		state: start_probability[state]
		* emission_probability[state].get(first_observation, 0.0)
		for state in states
	}

	for observation in observations[1:]:
		next_probabilities = {}
		pointers = {}

		for current_state in states:
			best_previous = max(
				states,
				key=lambda previous_state: (
					probabilities[previous_state]
					* transition_probability[previous_state].get(
						current_state, 0.0
					)
				),
			)
			next_probabilities[current_state] = (
				probabilities[best_previous]
				* transition_probability[best_previous].get(current_state, 0.0)
				* emission_probability[current_state].get(observation, 0.0)
			)
			pointers[current_state] = best_previous

		probabilities = next_probabilities
		backpointers.append(pointers)

	final_state = max(states, key=probabilities.get)
	best_probability = probabilities[final_state]
	path = [final_state]

	for pointers in reversed(backpointers):
		path.append(pointers[path[-1]])

	path.reverse()
	return path, best_probability


if __name__ == "__main__":
	states = ("Rainy", "Sunny")
	observations = ("walk", "shop", "clean")
	start = {"Rainy": 0.6, "Sunny": 0.4}
	transition = {
		"Rainy": {"Rainy": 0.7, "Sunny": 0.3},
		"Sunny": {"Rainy": 0.4, "Sunny": 0.6},
	}
	emission = {
		"Rainy": {"walk": 0.1, "shop": 0.4, "clean": 0.5},
		"Sunny": {"walk": 0.6, "shop": 0.3, "clean": 0.1},
	}

	sequence, probability = viterbi(
		observations, states, start, transition, emission
	)
	print("Most likely states:", sequence)
	print("Probability:", probability)
