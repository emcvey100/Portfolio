"""Fast Fourier transform implementation."""

from cmath import exp, pi
from typing import Iterable, List


def fft(values: Iterable[complex], inverse: bool = False) -> List[complex]:
    """Return the discrete Fourier transform of *values* in O(n log n) time.

    The input length must be a power of two.  Set ``inverse=True`` to
    calculate the inverse transform.
    """
    numbers = [complex(value) for value in values]
    n = len(numbers)

    if n == 0:
        return []
    if n & (n - 1):
        raise ValueError("FFT input length must be a power of two")
    if n == 1:
        return numbers

    even = fft(numbers[::2], inverse)
    odd = fft(numbers[1::2], inverse)
    sign = 1 if inverse else -1
    result = [0j] * n

    for k in range(n // 2):
        factor = exp(sign * 2j * pi * k / n) * odd[k]
        result[k] = even[k] + factor
        result[k + n // 2] = even[k] - factor

    if inverse:
        return [value / 2 for value in result]
    return result


def inverse_fft(values: Iterable[complex]) -> List[complex]:
    """Return the inverse discrete Fourier transform of *values*."""
    return fft(values, inverse=True)


if __name__ == "__main__":
    signal = [1, 2, 3, 4]
    transformed = fft(signal)
    print(transformed)
    print(inverse_fft(transformed))
