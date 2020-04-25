from unittest import TestCase

from binpacking.solver.solution import Solution


class SolutionTest(TestCase):
    def test_size(self) -> None:
        size: int = 3
        solution = Solution(size)
        self.assertEqual(len(solution), size)

    # Test get and set fitness
    def test_fitness(self) -> None:
        size: int = 3
        solution = Solution(size)
        fitness: float = 42.42
        solution.set_fitness(fitness)
        self.assertEqual(solution.get_fitness(), fitness)

    # Test the solution validator
    def test_fitness_is_valid(self) -> None:
        size: int = 3
        solution = Solution(size)
        self.assertFalse(solution.get_fitness_is_valid())
        fitness: float = 42.42
        solution.set_fitness(fitness)
        self.assertTrue(solution.get_fitness_is_valid())
