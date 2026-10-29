"""Principal Component Analysis (PCA).

PCA projects data onto orthogonal directions of greatest variance.
"""

import numpy as np


def principal_component_analysis(data, n_components=None):
    """Return the data projected onto its leading principal components.

    Parameters
    ----------
    data : array-like, shape (n_samples, n_features)
        Observations arranged by rows.
    n_components : int, optional
        Number of components to retain. Defaults to all components.

    Returns
    -------
    transformed : ndarray
        Centered data in principal-component coordinates.
    components : ndarray
        Principal directions, one per row.
    explained_variance : ndarray
        Variance explained by each selected component.
    """
    x = np.asarray(data, dtype=float)
    if x.ndim != 2:
        raise ValueError("data must be a two-dimensional array")
    if x.shape[0] < 2:
        raise ValueError("at least two samples are required")

    if n_components is None:
        n_components = min(x.shape)
    if not isinstance(n_components, (int, np.integer)) or not 1 <= n_components <= min(x.shape):
        raise ValueError("n_components must be between 1 and min(n_samples, n_features)")

    centered = x - x.mean(axis=0)
    _, singular_values, vh = np.linalg.svd(centered, full_matrices=False)
    components = vh[:n_components]
    explained_variance = singular_values[:n_components] ** 2 / (x.shape[0] - 1)
    transformed = centered @ components.T
    return transformed, components, explained_variance


if __name__ == "__main__":
    sample = np.array([[2, 0], [0, 2], [3, 1], [1, 3]])
    projected, directions, variance = principal_component_analysis(sample, 1)
    print("Projected data:\n", projected)
    print("Principal direction:\n", directions[0])
    print("Explained variance:", variance[0])