from unittest import TestCase

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution

class BinPacking2DTest(TestCase):
    def test_collision(self) -> None:
        instance = BinPacking2D([100,100], [[10,10], [10, 23]])
        solution = Solution(instance.get_instance_size())
        


        self.assertEqual(instance.collision(solution, 0, 1), True)

    def test_evaluation(self) -> None:
        # TODO: proper tests!
        self.assertEqual('foo'.upper(), 'FOO')
