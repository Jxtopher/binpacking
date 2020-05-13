from tests.base import BaseTestCase

from binpacking.solver.statistics import (
    Statistics,
    StatisticSolution,
    StatisticFitness,
    StatisticIteration,
)
from binpacking.solver.stop_criteria import StopCriteria, CriterionBudget
from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.solution import Solution, Coordinate

from binpacking.solver.backtracking import Backtracking


class BacktrackingTest(BaseTestCase):
    @BaseTestCase.timeConsumingTest()
    def test_run_big_instance(self) -> None:
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

        statistics = Statistics()
        statistics.add_statistic(StatisticIteration())
        statistics.add_statistic(StatisticFitness())
        statistics.add_statistic(StatisticSolution())
        stop_criteria = StopCriteria()
        stop_criteria.add_criterion(CriterionBudget(500))

        # backtracking = Backtracking(instance, statistics, stop_criteria)
        # backtracking.run(sol)

        backtracking = Backtracking(instance, statistics, stop_criteria, True)
        backtracking.run(sol)

    def test_run_small_instance(self) -> None:
        instance = BinPacking2D(Rectangle(2, 2), [Rectangle(1, 2), Rectangle(1, 2)],)
        sol = Solution(instance.get_instance_size())
        sol[0] = Coordinate(-1, -1)
        sol[1] = Coordinate(-1, -1)

        statistics = Statistics()
        stop_criteria = StopCriteria()

        backtracking = Backtracking(instance, statistics, stop_criteria)
        valid_solutions = backtracking.run(sol)

        self.assertEqual(
            str(valid_solutions),
            str(
                [
                    [(0, 0, 0), (1, 0, 0)],
                    [(0, 0, 90), (0, 1, 90)],
                    [(0, 1, 90), (0, 0, 90)],
                    [(1, 0, 0), (0, 0, 0)],
                ]
            ),
        )
