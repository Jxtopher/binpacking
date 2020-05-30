from tests.base import BaseTestCase

from binpacking.solver.statistics import Statistics
from binpacking.solver.stop_criteria import StopCriteria
from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.solution import Solution
from binpacking.solver.csp.backtracking import Backtracking
from binpacking.solver.domains import Domains


class BacktrackingTest(BaseTestCase):
    def test_backtracking(self) -> None:
        instance = BinPacking2D(
            Rectangle(2, 2), [Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1)],
        )
        sol = Solution(instance.get_instance_size())

        domains = Domains(instance)

        statistics = Statistics()
        stop_criteria = StopCriteria()

        backtracking = Backtracking(instance, statistics, stop_criteria)
        backtracking.run(sol, domains)
