"""Huffman coding: lossless text compression using prefix-free binary codes."""

from __future__ import annotations

from dataclasses import dataclass
import heapq
from itertools import count
from collections import Counter


@dataclass
class _Node:
	frequency: int
	character: str | None = None
	left: "_Node | None" = None
	right: "_Node | None" = None


def _build_tree(text: str) -> _Node | None:
	if not text:
		return None

	sequence = count()
	heap = [(_frequency, next(sequence), _Node(_frequency, character))
			for character, _frequency in Counter(text).items()]
	heapq.heapify(heap)

	while len(heap) > 1:
		left_frequency, _, left = heapq.heappop(heap)
		right_frequency, _, right = heapq.heappop(heap)
		parent = _Node(left_frequency + right_frequency, left=left, right=right)
		heapq.heappush(heap, (parent.frequency, next(sequence), parent))

	return heap[0][2]


def _codes(node: _Node | None, prefix: str = "") -> dict[str, str]:
	if node is None:
		return {}
	if node.character is not None:
		# A one-character input still needs a decodable bit representation.
		return {node.character: prefix or "0"}
	return {**_codes(node.left, prefix + "0"),
			**_codes(node.right, prefix + "1")}


def encode(text: str) -> tuple[str, dict[str, str]]:
	"""Return the Huffman bit string and the codebook needed to decode it."""
	codebook = _codes(_build_tree(text))
	return "".join(codebook[character] for character in text), codebook


def decode(bits: str, codebook: dict[str, str]) -> str:
	"""Decode a bit string using a codebook returned by :func:`encode`."""
	if any(bit not in "01" for bit in bits):
		raise ValueError("bits must contain only '0' and '1'")
	if not codebook:
		if bits:
			raise ValueError("cannot decode bits with an empty codebook")
		return ""

	reverse = {code: character for character, code in codebook.items()}
	result = []
	current = ""
	for bit in bits:
		current += bit
		if current in reverse:
			result.append(reverse[current])
			current = ""
	if current:
		raise ValueError("incomplete or invalid Huffman bit string")
	return "".join(result)


if __name__ == "__main__":
	message = "this is an example of huffman coding"
	encoded, table = encode(message)
	print(f"Original: {message}")
	print(f"Encoded:  {encoded}")
	print(f"Decoded:  {decode(encoded, table)}")
