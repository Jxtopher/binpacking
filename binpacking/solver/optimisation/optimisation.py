from abc import ABCMeta, abstractmethod
from typing import List

from binpacking.solver.solution import Solution
from binpacking.solver.domains import Domains


class Optimisation:

    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, sol: Solution, domains: Domains = None) -> List[Solution]:
        pass
