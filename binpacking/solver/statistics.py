from typing import List, Dict, Any, Optional
from abc import ABCMeta, abstractmethod
import copy

from binpacking.solver.data_structure.solution import Solution


class Statistic:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, sol: Solution) -> Dict[str, Any]:
        pass


class StatisticIteration(Statistic):
    def __init__(self) -> None:
        self.iteration = 0

    def run(self, sol: Solution) -> Dict[str, int]:
        self.iteration += 1
        return {'iteration': self.iteration - 1}


class StatisticFitness(Statistic):
    def run(self, sol: Solution) -> Dict[str, float]:
        return {'fitness': sol.get_fitness()}


class StatisticSolution(Statistic):
    def run(self, sol: Solution) -> Dict[str, str]:
        return {'sol': str(sol)}


class StatisticSolStar(Statistic):
    def __init__(self) -> None:
        self.sol_star: Solution = Solution(1)

    def run(self, sol: Solution) -> Dict[str, Solution]:
        if not self.sol_star.has_valid_fitness():
            self.sol_star = copy.deepcopy(sol)
        elif self.sol_star.get_fitness() < sol.get_fitness():
            self.sol_star = copy.deepcopy(sol)
        return {'sol_star': self.sol_star}


class Statistics:
    def __init__(self, *args: Statistic) -> None:
        self.statistics: List[Statistic] = []
        for arg in args:
            self.statistics.append(copy.deepcopy(arg))

    def run(self, sol: Solution) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        for statistic in self.statistics:
            result.update(statistic.run(sol))
        return result

    def add_statistic(self, statistic: Statistic) -> None:
        self.statistics.append(copy.deepcopy(statistic))
