"""Fisher's exact test for a 2x2 contingency table."""

from math import comb


def fisher_exact(table: list[list[int]], alternative: str = "two-sided") -> tuple[float, float]:
	"""Return the odds ratio and p-value for a 2x2 table."""
	if len(table) != 2 or any(len(row) != 2 for row in table):
		raise ValueError("table must be a 2x2 matrix")
	if alternative not in {"less", "greater", "two-sided"}:
		raise ValueError("alternative must be 'less', 'greater', or 'two-sided'")
	if any(isinstance(value, bool) or not isinstance(value, int) or value < 0
		   for row in table for value in row):
		raise ValueError("table entries must be non-negative integers")

	a, b = table[0]
	c, d = table[1]
	row_total = a + b
	column_total = a + c
	total = a + b + c + d
	denominator = comb(total, row_total)

	def probability(x: int) -> float:
		return (comb(column_total, x)
				* comb(total - column_total, row_total - x)
				/ denominator)

	lower = max(0, row_total - (total - column_total))
	upper = min(row_total, column_total)
	observed = probability(a)

	if alternative == "less":
		p_value = sum(probability(x) for x in range(lower, a + 1))
	elif alternative == "greater":
		p_value = sum(probability(x) for x in range(a, upper + 1))
	else:
		p_value = sum(
			probability(x) for x in range(lower, upper + 1)
			if probability(x) <= observed + 1e-12
		)

	odds_ratio = (float("inf") if b * c == 0 and a * d > 0
				  else a * d / (b * c) if b * c else float("nan"))
	return odds_ratio, min(1.0, p_value)


if __name__ == "__main__":
	odds_ratio, p_value = fisher_exact([[1, 9], [11, 3]])
	print(f"Odds ratio: {odds_ratio:.6g}")
	print(f"Two-sided p-value: {p_value:.6g}")
