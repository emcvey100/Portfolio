"""A small, dependency-light implementation of the Canny edge detector."""

from __future__ import annotations

import numpy as np


def _convolve(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
	"""Convolve a 2-D image using edge padding."""
	radius_y, radius_x = kernel.shape[0] // 2, kernel.shape[1] // 2
	padded = np.pad(image, ((radius_y, radius_y), (radius_x, radius_x)), mode="edge")
	result = np.zeros_like(image, dtype=float)
	for y in range(kernel.shape[0]):
		for x in range(kernel.shape[1]):
			result += kernel[y, x] * padded[y : y + image.shape[0], x : x + image.shape[1]]
	return result


def canny_edge_detector(
	image: np.ndarray,
	sigma: float = 1.4,
	low_threshold: float = 0.1,
	high_threshold: float = 0.2,
) -> np.ndarray:
	"""Return a binary edge image for a grayscale or RGB image.

	Thresholds in the range 0..1 are interpreted as fractions of the largest
	gradient magnitude; larger values are treated as absolute magnitudes.
	"""
	if sigma <= 0 or not 0 <= low_threshold <= high_threshold:
		raise ValueError("sigma must be positive and thresholds must be ordered")

	image = np.asarray(image, dtype=float)
	if image.ndim == 3:
		image = image[..., :3].mean(axis=2)
	if image.ndim != 2:
		raise ValueError("image must be a 2-D grayscale or 3-D RGB array")
	if image.size == 0:
		return np.zeros_like(image, dtype=np.uint8)

	image -= image.min()
	maximum = image.max()
	if maximum:
		image /= maximum

	radius = max(1, int(3 * sigma))
	coordinates = np.arange(-radius, radius + 1, dtype=float)
	gaussian = np.exp(-(coordinates**2) / (2 * sigma**2))
	gaussian /= gaussian.sum()
	smoothed = _convolve(_convolve(image, gaussian[:, None]), gaussian[None, :])

	gradient_x = _convolve(smoothed, np.array([[-1, 0, 1]], dtype=float))
	gradient_y = _convolve(smoothed, np.array([[-1], [0], [1]], dtype=float))
	magnitude = np.hypot(gradient_x, gradient_y)
	angle = np.rad2deg(np.arctan2(gradient_y, gradient_x)) % 180

	# Non-maximum suppression: retain only pixels along the local gradient.
	suppressed = np.zeros_like(magnitude)
	for y in range(1, magnitude.shape[0] - 1):
		for x in range(1, magnitude.shape[1] - 1):
			direction = angle[y, x]
			if direction < 22.5 or direction >= 157.5:
				first, second = magnitude[y, x - 1], magnitude[y, x + 1]
			elif direction < 67.5:
				first, second = magnitude[y - 1, x + 1], magnitude[y + 1, x - 1]
			elif direction < 112.5:
				first, second = magnitude[y - 1, x], magnitude[y + 1, x]
			else:
				first, second = magnitude[y - 1, x - 1], magnitude[y + 1, x + 1]
			if magnitude[y, x] >= first and magnitude[y, x] >= second:
				suppressed[y, x] = magnitude[y, x]

	scale = magnitude.max() if magnitude.max() else 1.0
	low = low_threshold * scale if low_threshold <= 1 else low_threshold
	high = high_threshold * scale if high_threshold <= 1 else high_threshold
	strong = suppressed >= high
	weak = (suppressed >= low) & ~strong

	# Hysteresis: weak pixels survive only when connected to a strong edge.
	edges = strong.copy()
	pending = list(zip(*np.nonzero(strong)))
	while pending:
		y, x = pending.pop()
		for yy in range(max(0, y - 1), min(edges.shape[0], y + 2)):
			for xx in range(max(0, x - 1), min(edges.shape[1], x + 2)):
				if weak[yy, xx] and not edges[yy, xx]:
					edges[yy, xx] = True
					pending.append((yy, xx))
	return (edges * 255).astype(np.uint8)


if __name__ == "__main__":
	print("Use canny_edge_detector(image) with a NumPy array.")
