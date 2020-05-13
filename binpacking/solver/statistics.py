from abc import ABCMeta, abstractmethod
from typing import List, Dict, Any
import copy
from binpacking.solver.solution import Solution


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


class Statistics:
    def __init__(self) -> None:
        self.statistics: List[Statistic] = []

    def run(self, sol: Solution) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        for statistic in self.statistics:
            result.update(statistic.run(sol))
        return result

    def add_statistic(self, statistic: Statistic) -> None:
        self.statistics.append(copy.deepcopy(statistic))
