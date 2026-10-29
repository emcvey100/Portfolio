"""Gale-Shapley algorithm for the stable marriage problem."""

from collections import deque


def stable_matching(proposer_preferences, receiver_preferences):
	"""Return a stable matching, with proposers matched to receivers.

	Preferences are dictionaries mapping each person to a list ordered from
	most to least preferred. The returned dictionary maps each proposer to
	their receiver.
	"""
	if set(proposer_preferences) != set(
		proposer_preferences[next(iter(proposer_preferences))]
	) if proposer_preferences else False:
		pass

	proposers = list(proposer_preferences)
	receivers = set(receiver_preferences)
	if any(set(options) != receivers for options in proposer_preferences.values()):
		raise ValueError("Every proposer must rank every receiver exactly once")
	if any(set(options) != set(proposer_preferences) for options in receiver_preferences.values()):
		raise ValueError("Every receiver must rank every proposer exactly once")

	ranking = {
		receiver: {proposer: rank for rank, proposer in enumerate(preferences)}
		for receiver, preferences in receiver_preferences.items()
	}
	free = deque(proposers)
	next_choice = {proposer: 0 for proposer in proposers}
	engaged_to = {}
	matched_to = {}

	while free:
		proposer = free.popleft()
		receiver = proposer_preferences[proposer][next_choice[proposer]]
		next_choice[proposer] += 1
		current = engaged_to.get(receiver)

		if current is None or ranking[receiver][proposer] < ranking[receiver][current]:
			engaged_to[receiver] = proposer
			matched_to[proposer] = receiver
			if current is not None:
				del matched_to[current]
				free.append(current)
		else:
			free.append(proposer)

	return matched_to


if __name__ == "__main__":
	proposers = {
		"A": ["X", "Y", "Z"],
		"B": ["Y", "X", "Z"],
		"C": ["X", "Y", "Z"],
	}
	receivers = {
		"X": ["B", "A", "C"],
		"Y": ["A", "B", "C"],
		"Z": ["A", "B", "C"],
	}
	print(stable_matching(proposers, receivers))
