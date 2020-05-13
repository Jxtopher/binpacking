from binpacking.solver.statistics import (
    Statistics,
    StatisticSolStar,
)
from binpacking.solver.stop_criteria import StopCriteria, CriterionBudget
from binpacking.solver.solution import Solution
from binpacking.solver.instance_loader import InstanceLoader
from binpacking.solver.backtracking import Backtracking
from binpacking.experimentations.experimentations import Experimentations


class ExpBacktracking:
    def run(self, budget: int, max_branches_explore: int = 50) -> float:
        instance = InstanceLoader.get_bin_packing("binpacking2d-90-1.json")
        sol_init = Solution(instance.get_instance_size())

        statistics = Statistics()
        statistics.add_statistic(StatisticSolStar())
        stop_criteria = StopCriteria()
        stop_criteria.add_criterion(CriterionBudget(budget))

        backtracking = Backtracking(instance, statistics, stop_criteria, randomize=True)
        backtracking.run_randomize(sol_init, 0, max_branches_explore)

        return float(statistics.run(sol_init)['sol_star'].get_fitness())
