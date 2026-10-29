"""Iterative Closest Point (ICP) for aligning two point clouds."""

import numpy as np


def _best_fit_transform(source, target):
	"""Return the rigid transform that best maps source points to target points."""
	source_centroid = source.mean(axis=0)
	target_centroid = target.mean(axis=0)
	source_centered = source - source_centroid
	target_centered = target - target_centroid

	covariance = source_centered.T @ target_centered
	u, _, vt = np.linalg.svd(covariance)
	rotation = vt.T @ u.T

	# Prevent reflection when the point clouds are mirrored by numerical noise.
	if np.linalg.det(rotation) < 0:
		vt[-1] *= -1
		rotation = vt.T @ u.T

	translation = target_centroid - rotation @ source_centroid
	return rotation, translation


def iterative_closest_point(source, target, max_iterations=100, tolerance=1e-6):
	"""Align ``source`` to ``target`` using rigid transforms.

	Returns ``(rotation, translation, mean_error, iterations)``. Both arrays
	must contain points with the same number of dimensions; nearest neighbors
	are found by a straightforward O(n*m) search.
	"""
	source = np.asarray(source, dtype=float)
	target = np.asarray(target, dtype=float)

	if source.ndim != 2 or target.ndim != 2:
		raise ValueError("source and target must be 2-D arrays of points")
	if source.shape[1] != target.shape[1] or not len(source) or not len(target):
		raise ValueError("point clouds must be non-empty and have equal dimensions")
	if max_iterations < 1 or tolerance < 0:
		raise ValueError("max_iterations must be positive and tolerance non-negative")

	dimension = source.shape[1]
	rotation = np.eye(dimension)
	translation = np.zeros(dimension)
	aligned = source.copy()
	previous_error = np.inf

	for iteration in range(1, max_iterations + 1):
		distances = np.sum((aligned[:, None, :] - target[None, :, :]) ** 2, axis=2)
		matches = target[np.argmin(distances, axis=1)]
		step_rotation, step_translation = _best_fit_transform(aligned, matches)

		aligned = aligned @ step_rotation.T + step_translation
		rotation = step_rotation @ rotation
		translation = step_rotation @ translation + step_translation

		error = np.mean(np.linalg.norm(aligned - matches, axis=1))
		if abs(previous_error - error) < tolerance:
			return rotation, translation, error, iteration
		previous_error = error

	return rotation, translation, previous_error, max_iterations


if __name__ == "__main__":
	points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
	angle = np.pi / 6
	known_rotation = np.array(
		[[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
	)
	transformed = points @ known_rotation.T + np.array([2.0, 1.0])
	rotation, translation, error, iterations = iterative_closest_point(points, transformed)
	print(f"rotation=\n{rotation}\ntranslation={translation}")
	print(f"error={error:.6g}, iterations={iterations}")
