"""Simple genetic algorithm for maximising a chromosome fitness function."""

from random import choice, choices, randint, random
from typing import Callable, Sequence, TypeVar


Gene = TypeVar("Gene")


def genetic_algorithm(
	fitness: Callable[[list[Gene]], float],
	gene_pool: Sequence[Gene],
	chromosome_length: int,
	*,
	population_size: int = 100,
	generations: int = 200,
	mutation_rate: float = 0.01,
) -> list[Gene]:
	"""Find and return the chromosome with the highest fitness score."""
	if not gene_pool:
		raise ValueError("gene_pool cannot be empty")
	if chromosome_length < 1 or population_size < 2 or generations < 0:
		raise ValueError("invalid chromosome length, population size, or generations")
	if not 0 <= mutation_rate <= 1:
		raise ValueError("mutation_rate must be between 0 and 1")

	def create_chromosome() -> list[Gene]:
		return [choice(gene_pool) for _ in range(chromosome_length)]

	population = [create_chromosome() for _ in range(population_size)]
	best = max(population, key=fitness).copy()

	for _ in range(generations):
		population.sort(key=fitness, reverse=True)
		if fitness(population[0]) > fitness(best):
			best = population[0].copy()

		survivors = population[: max(2, population_size // 2)]
		lowest_score = fitness(survivors[-1])
		weights = [fitness(item) - lowest_score + 1e-12 for item in survivors]
		next_population = [survivors[0].copy(), survivors[1].copy()]

		while len(next_population) < population_size:
			parent_a, parent_b = choices(survivors, weights=weights, k=2)
			point = randint(1, chromosome_length - 1) if chromosome_length > 1 else 1
			child = parent_a[:point] + parent_b[point:]
			child = [
				choice(gene_pool) if random() < mutation_rate else gene
				for gene in child
			]
			next_population.append(child)
		population = next_population

	return max([best, *population], key=fitness)


if __name__ == "__main__":
	target = "GENETIC ALGORITHM"

	def score(chromosome: list[str]) -> float:
		return sum(gene == expected for gene, expected in zip(chromosome, target))

	answer = genetic_algorithm(score, list(" GENETIC ALGORITHM"), len(target))
	print("".join(answer))
