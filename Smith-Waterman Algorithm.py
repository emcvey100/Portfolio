"""Smith-Waterman local sequence alignment."""


def smith_waterman(
	sequence_a: str,
	sequence_b: str,
	match: int = 2,
	mismatch: int = -1,
	gap: int = -1,
) -> tuple[int, str, str]:
	"""Return the best local alignment score and aligned subsequences."""
	rows, columns = len(sequence_a) + 1, len(sequence_b) + 1
	scores = [[0] * columns for _ in range(rows)]
	best_score = 0
	best_cell = (0, 0)

	for i in range(1, rows):
		for j in range(1, columns):
			diagonal = scores[i - 1][j - 1] + (
				match if sequence_a[i - 1] == sequence_b[j - 1] else mismatch
			)
			scores[i][j] = max(
				0,
				diagonal,
				scores[i - 1][j] + gap,
				scores[i][j - 1] + gap,
			)
			if scores[i][j] > best_score:
				best_score = scores[i][j]
				best_cell = (i, j)

	aligned_a, aligned_b = [], []
	i, j = best_cell
	while i > 0 and j > 0 and scores[i][j] > 0:
		score = scores[i][j]
		diagonal_score = scores[i - 1][j - 1] + (
			match if sequence_a[i - 1] == sequence_b[j - 1] else mismatch
		)
		if score == diagonal_score:
			aligned_a.append(sequence_a[i - 1])
			aligned_b.append(sequence_b[j - 1])
			i -= 1
			j -= 1
		elif score == scores[i - 1][j] + gap:
			aligned_a.append(sequence_a[i - 1])
			aligned_b.append("-")
			i -= 1
		else:
			aligned_a.append("-")
			aligned_b.append(sequence_b[j - 1])
			j -= 1

	return best_score, "".join(reversed(aligned_a)), "".join(reversed(aligned_b))


if __name__ == "__main__":
	score, first, second = smith_waterman("ACACACTA", "AGCACACA")
	print(f"Score: {score}\n{first}\n{second}")
