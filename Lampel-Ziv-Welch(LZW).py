"""Lempel-Ziv-Welch (LZW) compression and decompression."""


def compress(text: str) -> list[int]:
	"""Compress *text* into a sequence of dictionary codes."""
	if not isinstance(text, str):
		raise TypeError("text must be a string")
	if not text:
		return []

	# Start with every character that occurs in the input.  This keeps the
	# function useful for Unicode text as well as ordinary ASCII strings.
	dictionary = {character: code for code, character in enumerate(set(text))}
	next_code = len(dictionary)
	current = text[0]
	compressed = []

	for character in text[1:]:
		candidate = current + character
		if candidate in dictionary:
			current = candidate
		else:
			compressed.append(dictionary[current])
			dictionary[candidate] = next_code
			next_code += 1
			current = character

	compressed.append(dictionary[current])
	return compressed


def decompress(codes: list[int], symbols: str) -> str:
	"""Decompress LZW *codes* using the original input's character set.

	``symbols`` must contain the distinct characters used to create the
	codes.  Pass ``""`` when decompressing an empty sequence.
	"""
	if not codes:
		return ""
	if not symbols:
		raise ValueError("symbols cannot be empty when codes are provided")

	dictionary = {
		code: character for code, character in enumerate(set(symbols))
	}
	try:
		previous = dictionary[codes[0]]
	except (KeyError, IndexError) as error:
		raise ValueError("invalid LZW code") from error

	result = [previous]
	next_code = len(dictionary)

	for code in codes[1:]:
		if code in dictionary:
			entry = dictionary[code]
		elif code == next_code:
			# The encoder can reference the entry being created in this step.
			entry = previous + previous[0]
		else:
			raise ValueError("invalid LZW code")

		result.append(entry)
		dictionary[next_code] = previous + entry[0]
		next_code += 1
		previous = entry

	return "".join(result)


if __name__ == "__main__":
	sample = "TOBEORNOTTOBEORTOBEORNOT"
	codes = compress(sample)
	print("Codes:", codes)
	print("Decoded:", decompress(codes, sample))
