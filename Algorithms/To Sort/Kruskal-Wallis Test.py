"""Kruskal-Wallis H test for comparing three or more independent samples."""

from math import erfc, sqrt


def kruskal_wallis(*samples):
	"""Return ``(h_statistic, p_value)`` for independent samples.

	The p-value uses the chi-square approximation with ``k - 1`` degrees of
	freedom. Tied observations receive their average rank.
	"""
	if len(samples) < 2 or any(not sample for sample in samples):
		raise ValueError("provide at least two non-empty samples")

	values = [(value, group) for group, sample in enumerate(samples)
			  for value in sample]
	values.sort(key=lambda item: item[0])

	ranks = [0.0] * len(values)
	tie_sizes = []
	index = 0
	while index < len(values):
		end = index + 1
		while end < len(values) and values[end][0] == values[index][0]:
			end += 1
		rank = (index + 1 + end) / 2.0
		for position in range(index, end):
			ranks[position] = rank
		tie_sizes.append(end - index)
		index = end

	group_rank_sums = [0.0] * len(samples)
	for rank, (_, group) in zip(ranks, values):
		group_rank_sums[group] += rank

	total = len(values)
	h = (12 / (total * (total + 1))) * sum(
		rank_sum ** 2 / len(sample)
		for rank_sum, sample in zip(group_rank_sums, samples)
	) - 3 * (total + 1)

	tie_correction = 1 - sum(size ** 3 - size for size in tie_sizes) / (
		total ** 3 - total
	)
	if tie_correction:
		h /= tie_correction

	degrees_of_freedom = len(samples) - 1
	# For an integer chi-square degree of freedom, the survival function is
	# computed without requiring a third-party statistics package.
	p_value = _chi_square_survival(h, degrees_of_freedom)
	return h, p_value


def _chi_square_survival(value, degrees_of_freedom):
	"""Chi-square survival function for the common integer degrees of freedom."""
	if degrees_of_freedom == 1:
		return erfc(sqrt(max(value, 0) / 2))
	term = 1.0
	series = 1.0
	for number in range(1, degrees_of_freedom // 2):
		term *= max(value, 0) / (2 * number)
		series += term
	return (2 ** (-degrees_of_freedom / 2) *
			max(value, 0) ** (degrees_of_freedom / 2) /
			_gamma(degrees_of_freedom / 2) * series) if degrees_of_freedom % 2 else __import__("math").exp(-value / 2) * series


def _gamma(value):
	from math import gamma
	return gamma(value)
