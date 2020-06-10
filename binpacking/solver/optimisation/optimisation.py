from abc import ABCMeta, abstractmethod
from typing import List

from binpacking.solver.solution import Solution


class Optimisation:

    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, sol: Solution) -> List[Solution]:
        pass
