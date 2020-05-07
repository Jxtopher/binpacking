from tests.base import BaseTestCase

from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.backtracking import Backtracking


class BacktrackingTest(BaseTestCase):
    def test_run(self) -> None:
        instance = BinPacking2D(
            Rectangle(100, 100),
            [
                Rectangle(30, 40),
                Rectangle(70, 30),
                Rectangle(30, 30),
                Rectangle(40, 70),
                Rectangle(30, 20),
                Rectangle(30, 70),
            ],
        )
        sol = Solution(instance.get_instance_size())
        sol[0] = Coordinate(-1, -1)
        sol[1] = Coordinate(-1, -1)
        sol[2] = Coordinate(-1, -1)
        sol[3] = Coordinate(-1, -1)
        sol[4] = Coordinate(-1, -1)
        sol[5] = Coordinate(-1, -1)

        backtracking = Backtracking(instance)
        backtracking.run(sol)
