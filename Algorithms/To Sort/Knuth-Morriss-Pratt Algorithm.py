"""Knuth-Morris-Pratt string-search algorithm."""


def _build_lps(pattern: str) -> list[int]:
	"""Build the longest-proper-prefix/suffix table for *pattern*."""
	lps = [0] * len(pattern)
	prefix_length = 0
	index = 1

	while index < len(pattern):
		if pattern[index] == pattern[prefix_length]:
			prefix_length += 1
			lps[index] = prefix_length
			index += 1
		elif prefix_length:
			prefix_length = lps[prefix_length - 1]
		else:
			index += 1

	return lps


def kmp_search(text: str, pattern: str) -> int:
	"""Return the first index of *pattern* in *text*, or -1 if absent."""
	if not pattern:
		return 0

	lps = _build_lps(pattern)
	text_index = pattern_index = 0

	while text_index < len(text):
		if text[text_index] == pattern[pattern_index]:
			text_index += 1
			pattern_index += 1
			if pattern_index == len(pattern):
				return text_index - pattern_index
		elif pattern_index:
			pattern_index = lps[pattern_index - 1]
		else:
			text_index += 1

	return -1


def kmp_find_all(text: str, pattern: str) -> list[int]:
	"""Return the starting indexes of every occurrence of *pattern*."""
	if not pattern:
		return list(range(len(text) + 1))

	lps = _build_lps(pattern)
	matches = []
	text_index = pattern_index = 0

	while text_index < len(text):
		if text[text_index] == pattern[pattern_index]:
			text_index += 1
			pattern_index += 1
			if pattern_index == len(pattern):
				matches.append(text_index - pattern_index)
				pattern_index = lps[pattern_index - 1]
		elif pattern_index:
			pattern_index = lps[pattern_index - 1]
		else:
			text_index += 1

	return matches
