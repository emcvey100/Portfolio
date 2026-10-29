"""Radix-2 Cooley-Tukey Fast Fourier Transform."""

from cmath import exp, pi
from typing import Sequence


def fft(values: Sequence[complex], inverse: bool = False) -> list[complex]:
	"""Return the discrete Fourier transform of ``values`` in O(n log n).

	The radix-2 algorithm requires the input length to be a power of two.
	Pass ``inverse=True`` to compute the inverse transform.
	"""
	n = len(values)
	if n == 0:
		return []
	if n & (n - 1):
		raise ValueError("input length must be a power of two")
	if n == 1:
		return [complex(values[0])]

	even = fft(values[::2], inverse)
	odd = fft(values[1::2], inverse)
	sign = 1 if inverse else -1
	result = [0j] * n

	for k in range(n // 2):
		twiddle = exp(sign * 2j * pi * k / n) * odd[k]
		result[k] = even[k] + twiddle
		result[k + n // 2] = even[k] - twiddle

	if inverse:
		return [value / 2 for value in result]
	return result


if __name__ == "__main__":
	signal = [1, 2, 3, 4]
	transformed = fft(signal)
	print(transformed)
	print(fft(transformed, inverse=True))
