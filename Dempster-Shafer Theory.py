"""Small, dependency-free implementation of Dempster-Shafer theory."""

from collections.abc import Iterable, Mapping


MassFunction = dict[frozenset, float]


def _validate(mass: Mapping[frozenset, float]) -> None:
	"""Validate a basic probability assignment."""
	if not mass:
		raise ValueError("a mass function cannot be empty")
	if any(not isinstance(focal_set, frozenset) for focal_set in mass):
		raise TypeError("focal elements must be frozenset instances")
	if any(value < 0 for value in mass.values()):
		raise ValueError("masses cannot be negative")
	if not abs(sum(mass.values()) - 1.0) <= 1e-9:
		raise ValueError("masses must sum to 1")


def mass_function(assignments: Mapping[Iterable, float]) -> MassFunction:
	"""Build a validated mass function from iterable focal elements."""
	result = {
		frozenset(focal_set): float(value)
		for focal_set, value in assignments.items()
	}
	_validate(result)
	return result


def combine(first: Mapping[frozenset, float], second: Mapping[frozenset, float]) -> MassFunction:
	"""Combine two independent mass functions using Dempster's rule."""
	_validate(first)
	_validate(second)
	result: dict[frozenset, float] = {}
	conflict = 0.0

	for first_set, first_mass in first.items():
		for second_set, second_mass in second.items():
			product = first_mass * second_mass
			intersection = first_set & second_set
			if intersection:
				result[intersection] = result.get(intersection, 0.0) + product
			else:
				conflict += product

	if conflict >= 1.0:
		raise ValueError("Dempster's rule is undefined when conflict is 1")
	return {focal_set: value / (1.0 - conflict) for focal_set, value in result.items()}


def belief(mass: Mapping[frozenset, float], proposition: Iterable) -> float:
	"""Return Bel(A): mass assigned to subsets of proposition A."""
	_validate(mass)
	proposition = frozenset(proposition)
	return sum(value for focal_set, value in mass.items() if focal_set <= proposition)


def plausibility(mass: Mapping[frozenset, float], proposition: Iterable) -> float:
	"""Return Pl(A): mass assigned to sets intersecting proposition A."""
	_validate(mass)
	proposition = frozenset(proposition)
	return sum(value for focal_set, value in mass.items() if focal_set & proposition)


if __name__ == "__main__":
	frame = frozenset({"sunny", "rainy"})
	source_a = mass_function({frozenset({"sunny"}): 0.6, frame: 0.4})
	source_b = mass_function({frozenset({"sunny"}): 0.7, frame: 0.3})
	combined = combine(source_a, source_b)
	print("Combined masses:", combined)
	print("Bel(sunny):", belief(combined, {"sunny"}))
	print("Pl(sunny):", plausibility(combined, {"sunny"}))
