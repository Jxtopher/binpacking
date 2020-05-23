from tests.base import BaseTestCase

from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.arcconsistency.ac3 import AC3


class AC3Test(BaseTestCase):
    def test_ac3_with_all_fitting_inputs(self) -> None:
        instance = BinPacking2D(
            Rectangle(100, 100), [Rectangle(10, 10), Rectangle(20, 20), Rectangle(10, 30)],
        )
        sol = Solution(instance.get_instance_size())

        ac3 = AC3(instance)
        domains = ac3.run(sol)
        self.assertEqual(sum(len(sub_domain) for sub_domain in domains.values()), 42609)

    def test_ac3_without_all_fitting_inputs(self) -> None:
        instance = BinPacking2D(
            Rectangle(10, 10), [Rectangle(1, 1), Rectangle(8, 8), Rectangle(3, 3)],
        )
        sol = Solution(instance.get_instance_size())

        ac3 = AC3(instance)
        domains = ac3.run(sol)
        self.assertEqual(sum(len(sub_domain) for sub_domain in domains.values()), 251)
