from tests.base import BaseTestCase
import copy

from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.solution import Solution
from binpacking.solver.metaheuristic.neighborhood import Neighborhood


class NeighborhoodTest(BaseTestCase):
    def test_find_random_neighbor(self) -> None:
        pass

    def test_find_one_mutation_neighbor(self) -> None:
        pass

    def test_find_two_mutation_neighbor(self) -> None:
        instance = BinPacking2D(
            Rectangle(5, 5), [Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1)]
        )

        sol = Solution(instance.get_instance_size())
        sol_tmp = copy.deepcopy(sol)
        Neighborhood.find_two_mutation_neighbor(instance, sol)

        cpt = 0
        for i in range(len(sol)):
            if (
                sol[i].x != sol_tmp[i].x
                or sol[i].y != sol_tmp[i].y
                or sol[i].is_rotated != sol_tmp[i].is_rotated
            ):
                cpt += 1

        self.assertTrue(cpt == 2)
