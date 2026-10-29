"""Calculate the Vapnik-Chervonenkis dimension of a finite binary class."""

from itertools import combinations
from typing import Iterable, Sequence


def vc_dimension(hypotheses: Iterable[Sequence[int]]) -> int:
	"""Return the largest size of a subset shattered by ``hypotheses``.

	Each hypothesis is a sequence of 0/1 labels over the same finite domain.
	A subset is shattered when its hypotheses realize all ``2 ** k`` labelings.
	"""
	rows = [tuple(hypothesis) for hypothesis in hypotheses]
	if not rows:
		raise ValueError("hypotheses must not be empty")

	domain_size = len(rows[0])
	if any(len(row) != domain_size for row in rows):
		raise ValueError("all hypotheses must have the same length")
	if any(label not in (0, 1) for row in rows for label in row):
		raise ValueError("hypotheses must contain only 0 or 1")

	for size in range(domain_size, -1, -1):
		for points in combinations(range(domain_size), size):
			realized = {tuple(row[index] for index in points) for row in rows}
			if len(realized) == 2 ** size:
				return size
	return 0


if __name__ == "__main__":
	# All thresholds on three ordered points have VC dimension 1.
	thresholds = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))
	print(vc_dimension(thresholds))
