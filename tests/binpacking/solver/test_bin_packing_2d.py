from unittest import TestCase

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution

class BinPacking2DTest(TestCase):
    def test_collision(self) -> None:
        instance = BinPacking2D([100,100], [[6,6], [2, 2]])
        solution = Solution(instance.get_instance_size())
        self.assertEqual(instance.collision(solution, 0, 1), True)

        solution[0] = [0,0,0]
        solution[1] = [6,6,0]
        self.assertEqual(instance.collision(solution, 0, 1), False)

        solution[0] = [0,0,0]
        solution[1] = [0,6,0]
        self.assertEqual(instance.collision(solution, 0, 1), False)

        solution[0] = [0,0,0]
        solution[1] = [5,2,0]
        self.assertEqual(instance.collision(solution, 0, 1), True)

        solution[0] = [0,0,0]
        solution[1] = [2,5,0]
        self.assertEqual(instance.collision(solution, 0, 1), True)

        solution[0] = [2,0,0]
        solution[1] = [1,2,0]
        self.assertEqual(instance.collision(solution, 0, 1), True)

        solution[0] = [2,0,0]
        solution[1] = [0,2,0]
        self.assertEqual(instance.collision(solution, 1, 0), False)

        solution[0] = [2,0,0]
        solution[1] = [0,2,0]
        self.assertEqual(instance.collision(solution, 0, 1), False)
    def test_evaluation(self) -> None:
        # TODO: proper tests!
        self.assertEqual('foo'.upper(), 'FOO')
