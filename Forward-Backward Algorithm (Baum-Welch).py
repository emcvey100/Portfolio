"""Forward-backward algorithm for a discrete Hidden Markov Model."""


def forward_backward(observations, initial, transition, emission):
	"""Return forward probabilities, backward probabilities, and likelihood.

	``transition[i][j]`` is P(state j | state i), and
	``emission[i][symbol]`` is P(symbol | state i).
	"""
	observations = list(observations)
	state_count = len(initial)
	if not observations or state_count == 0:
		raise ValueError("observations and initial probabilities must not be empty")
	if len(transition) != state_count or any(
			len(row) != state_count for row in transition):
		raise ValueError("transition must be a square matrix")

	forward = []
	scales = []

	values = [initial[i] * emission[i][observations[0]]
			  for i in range(state_count)]
	scale = sum(values)
	if scale <= 0:
		raise ValueError("observation sequence has zero probability")
	forward.append([value / scale for value in values])
	scales.append(scale)

	for observation in observations[1:]:
		values = [emission[j][observation] * sum(
			forward[-1][i] * transition[i][j]
			for i in range(state_count)) for j in range(state_count)]
		scale = sum(values)
		if scale <= 0:
			raise ValueError("observation sequence has zero probability")
		forward.append([value / scale for value in values])
		scales.append(scale)

	backward = [[0.0] * state_count for _ in observations]
	backward[-1] = [1.0] * state_count
	for time in range(len(observations) - 2, -1, -1):
		next_observation = observations[time + 1]
		backward[time] = [sum(
			transition[i][j] * emission[j][next_observation] *
			backward[time + 1][j] for j in range(state_count)) / scales[time + 1]
			for i in range(state_count)]

	likelihood = 1.0
	for scale in scales:
		likelihood *= scale
	return forward, backward, likelihood


if __name__ == "__main__":
	forward, backward, likelihood = forward_backward(
		observations=[0, 1, 0],
		initial=[0.6, 0.4],
		transition=[[0.7, 0.3], [0.4, 0.6]],
		emission=[[0.1, 0.9], [0.6, 0.4]],
	)
	print("Likelihood:", likelihood)
	print("Forward:", forward)
	print("Backward:", backward)
