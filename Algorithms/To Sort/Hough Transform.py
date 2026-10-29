"""A simple Hough transform for detecting straight lines in an edge image."""

from __future__ import annotations

import numpy as np


def hough_transform(edges: np.ndarray, theta_step: float = 1.0):
	"""Return the accumulator and the angles/distances represented by it.

	``edges`` may be a boolean or grayscale image; every non-zero pixel is
	treated as an edge.  A line is represented by ``rho = x*cos(theta) +
	y*sin(theta)`` with theta in ``[-90, 90)`` degrees.
	"""
	if edges.ndim != 2:
		raise ValueError("edges must be a two-dimensional image")
	if theta_step <= 0 or theta_step > 180:
		raise ValueError("theta_step must be greater than 0 and at most 180")

	height, width = edges.shape
	thetas = np.deg2rad(np.arange(-90.0, 90.0, theta_step))
	diagonal = int(np.ceil(np.hypot(height - 1, width - 1)))
	rhos = np.arange(-diagonal, diagonal + 1)
	accumulator = np.zeros((len(rhos), len(thetas)), dtype=np.uint64)

	y_coords, x_coords = np.nonzero(edges)
	if len(x_coords) == 0:
		return accumulator, rhos, thetas

	rho_values = x_coords[:, None] * np.cos(thetas) + y_coords[:, None] * np.sin(thetas)
	rho_indices = np.rint(rho_values).astype(int) + diagonal
	theta_indices = np.broadcast_to(
		np.arange(len(thetas)), rho_indices.shape
	)
	np.add.at(accumulator, (rho_indices.ravel(), theta_indices.ravel()), 1)
	return accumulator, rhos, thetas


def detect_lines(
	edges: np.ndarray,
	threshold: int,
	theta_step: float = 1.0,
) -> list[tuple[int, float]]:
	"""Return ``(votes, theta_degrees)`` for accumulator cells above threshold."""
	accumulator, rhos, thetas = hough_transform(edges, theta_step)
	rows, columns = np.nonzero(accumulator >= threshold)
	lines = [(int(accumulator[row, column]), float(np.rad2deg(thetas[column])))
			 for row, column in zip(rows, columns)]
	return sorted(lines, reverse=True)


if __name__ == "__main__":
	# Small example: a diagonal line in a 20 x 20 edge image.
	image = np.zeros((20, 20), dtype=bool)
	np.fill_diagonal(image, True)
	accumulator, rhos, thetas = hough_transform(image)
	peak = np.unravel_index(np.argmax(accumulator), accumulator.shape)
	print(f"strongest line: rho={rhos[peak[0]]}, "
		  f"theta={np.rad2deg(thetas[peak[1]]):.1f}°, "
		  f"votes={accumulator[peak]:d}")
