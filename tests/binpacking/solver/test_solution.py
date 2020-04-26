from unittest import TestCase

from binpacking.solver.solution import Solution


class SolutionTest(TestCase):
    def test_solution_size(self) -> None:
        size: int = 3
        solution = Solution(size)
        self.assertEqual(len(solution), size)

    def test_fitness_getter_setter(self) -> None:
        size: int = 3
        solution = Solution(size)
        fitness: float = 42.42
        solution.set_fitness(fitness)
        self.assertEqual(solution.get_fitness(), fitness)

    def test_solution_validation_with_valid_fitness(self) -> None:
        size: int = 3
        solution = Solution(size)
        self.assertFalse(solution.has_valid_fitness())
        fitness: float = 42.42
        solution.set_fitness(fitness)
        self.assertTrue(solution.has_valid_fitness())
