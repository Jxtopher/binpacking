from unittest import TestCase

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution


class BinPacking2DTest(TestCase):
    def test_has_collision(self) -> None:
        instance = BinPacking2D((10, 10), [(6, 6), (2, 2)])
        solution = Solution(instance.get_instance_size())
        self.assertTrue(instance.has_collision(solution, 0, 1))

        solution[0] = (0, 0, 0)
        solution[1] = (6, 6, 0)
        self.assertFalse(instance.has_collision(solution, 0, 1))

        solution[0] = (0, 0, 0)
        solution[1] = (0, 6, 0)
        self.assertFalse(instance.has_collision(solution, 0, 1))

        solution[0] = (0, 0, 0)
        solution[1] = (5, 2, 0)
        self.assertTrue(instance.has_collision(solution, 0, 1))

        solution[0] = (0, 0, 0)
        solution[1] = (2, 5, 0)
        self.assertTrue(instance.has_collision(solution, 0, 1))

        solution[0] = (2, 0, 0)
        solution[1] = (1, 2, 0)
        self.assertTrue(instance.has_collision(solution, 0, 1))

        solution[0] = (2, 0, 0)
        solution[1] = (0, 2, 0)
        self.assertFalse(instance.has_collision(solution, 1, 0))

        solution[0] = (2, 0, 0)
        solution[1] = (0, 2, 0)
        self.assertFalse(instance.has_collision(solution, 0, 1))

    def test_is_inside(self) -> None:
        instance = BinPacking2D((100, 100), [(6, 6)])
        solution = Solution(instance.get_instance_size())

        solution[0] = (0, 0, 0)
        self.assertTrue(instance.is_inside(solution, 0))

        solution[0] = (100, 0, 0)
        self.assertFalse(instance.is_inside(solution, 0))

        solution[0] = (99, 99, 0)
        self.assertFalse(instance.is_inside(solution, 0))

        solution[0] = (93, 93, 0)
        self.assertTrue(instance.is_inside(solution, 0))

    def test_evaluate(self) -> None:
        instance = BinPacking2D((100, 100), [(1, 1), (1, 1), (1, 1), (1, 1)])
        solution = Solution(instance.get_instance_size())
        solution[0] = (0, 0, 0)
        solution[1] = (1, 1, 0)
        solution[2] = (2, 2, 0)
        solution[3] = (3, 3, 0)

        instance.evaluate(solution)
        print(solution.get_fitness())

        # TODO: check something
