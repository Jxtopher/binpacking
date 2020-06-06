from tests.base import BaseTestCase
from binpacking.solver.solution import Solution
from binpacking.solver.statistics import Statistics, StatisticIteration, StatisticFitness


class StatisticsTest(BaseTestCase):
    def test_statistics(self) -> None:
        iteration = StatisticIteration()

        fitness = StatisticFitness()

        statistics = Statistics()
        statistics.add_statistic(iteration)
        statistics.add_statistic(fitness)

        expected_size = 4
        sol = Solution(expected_size)
        sol.set_fitness(float(42))

        r = statistics.run(sol)
        self.assertTrue(r['iteration'] == 0)

        r = statistics.run(sol)
        self.assertTrue(r['iteration'] == 1)
