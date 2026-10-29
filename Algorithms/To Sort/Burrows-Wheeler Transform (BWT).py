"""Burrows-Wheeler Transform (BWT) implementation."""


def bwt(text: str, sentinel: str = "$") -> tuple[str, int]:
	"""Return the BWT of *text* and the row containing the original text.

	The sentinel must not occur in the input and sorts before other symbols.
	"""
	if len(sentinel) != 1 or sentinel in text:
		raise ValueError("sentinel must be one character not in text")

	text = text + sentinel
	rotations = [text[i:] + text[:i] for i in range(len(text))]
	rotations.sort()
	return "".join(rotation[-1] for rotation in rotations), rotations.index(text)


def inverse_bwt(last_column: str, row: int, sentinel: str = "$") -> str:
	"""Reconstruct the original text from a BWT result."""
	if len(sentinel) != 1 or last_column.count(sentinel) != 1:
		raise ValueError("last_column must contain exactly one sentinel")
	if not 0 <= row < len(last_column):
		raise ValueError("row is out of range")

	table = [""] * len(last_column)
	for _ in last_column:
		table = sorted(
			last_column[i] + table[i] for i in range(len(last_column))
		)

	result = table[row]
	if not result.endswith(sentinel):
		raise ValueError("invalid BWT data")
	return result[:-1]


if __name__ == "__main__":
	encoded, original_row = bwt("BANANA")
	print(encoded, original_row)
	print(inverse_bwt(encoded, original_row))
