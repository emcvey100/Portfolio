"""One-sample and two-sample Kolmogorov-Smirnov tests."""

from math import exp, sqrt


def _p_value(statistic, effective_n):
	"""Return the asymptotic upper-tail probability for a KS statistic."""
	if statistic <= 0:
		return 1.0
	x = (sqrt(effective_n) + 0.12 + 0.11 / sqrt(effective_n)) * statistic
	probability = 2 * sum(
		(-1) ** (k - 1) * exp(-2 * k * k * x * x)
		for k in range(1, 101)
	)
	return max(0.0, min(1.0, probability))


def one_sample_ks(sample, cdf):
	"""Compare ``sample`` with a continuous distribution's CDF.

	Returns ``(D, p_value)``. ``cdf`` accepts one observation and returns
	its cumulative probability.
	"""
	values = sorted(sample)
	if not values:
		raise ValueError("sample must not be empty")

	n = len(values)
	d_plus = max((i + 1) / n - cdf(value) for i, value in enumerate(values))
	d_minus = max(cdf(value) - i / n for i, value in enumerate(values))
	statistic = max(d_plus, d_minus)
	return statistic, _p_value(statistic, n)


def two_sample_ks(sample_a, sample_b):
	"""Compare two independent samples with the two-sample KS test.

	Returns ``(D, p_value)`` using the asymptotic approximation.
	"""
	a, b = sorted(sample_a), sorted(sample_b)
	if not a or not b:
		raise ValueError("samples must not be empty")

	points = sorted(set(a + b))
	n, m = len(a), len(b)
	statistic = max(
		abs(sum(value <= point for value in a) / n -
			sum(value <= point for value in b) / m)
		for point in points
	)
	effective_n = n * m / (n + m)
	return statistic, _p_value(statistic, effective_n)


if __name__ == "__main__":
	# Example: test observations against Uniform(0, 1).
	observations = [0.05, 0.18, 0.31, 0.47, 0.62, 0.79, 0.91]
	statistic, p_value = one_sample_ks(
		observations, lambda x: max(0.0, min(1.0, x))
	)
	print(f"D = {statistic:.4f}, p-value = {p_value:.4f}")
