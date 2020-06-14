from tests.base import BaseTestCase
from binpacking.solver.data_structure.solution import Solution


class SolutionTest(BaseTestCase):
    def test_solution_size(self) -> None:
        expected_size: int = 3
        sol = Solution(expected_size)
        self.assertEqual(len(sol), expected_size)

    def test_fitness_getter_setter(self) -> None:
        size: int = 3
        sol = Solution(size)
        fitness: float = 42.42
        sol.set_fitness(fitness)
        self.assertEqual(sol.get_fitness(), fitness)

    def test_solution_validation_with_valid_fitness(self) -> None:
        size: int = 3
        sol = Solution(size)
        self.assertFalse(sol.has_valid_fitness())
        fitness: float = 42.42
        sol.set_fitness(fitness)
        self.assertTrue(sol.has_valid_fitness())
