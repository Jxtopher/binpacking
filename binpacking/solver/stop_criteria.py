from abc import ABCMeta, abstractmethod
from typing import List
import copy
from binpacking.solver.solution import Solution


class Criterion:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, sol: Solution) -> bool:
        pass


class Budget(Criterion):
    def __init__(self, max_iterations: int):
        self.max_iterations = max_iterations
        self.iteration = 0

    def run(self, sol: Solution) -> bool:
        print("X")
        print(self.iteration)
        self.iteration += 1
        return self.iteration - 1 < self.max_iterations


class StopCriteria:
    def __init__(self) -> None:
        self.criterions: List[Criterion] = []

    def run(self, sol: Solution) -> bool:
        result = True
        for criterion in self.criterions:
            result = criterion.run(sol) and result
        return result

    def add_criterion(self, criterion: Criterion) -> None:
        self.criterions.append(copy.deepcopy(criterion))