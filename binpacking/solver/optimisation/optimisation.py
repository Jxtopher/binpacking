from abc import ABCMeta, abstractmethod
from typing import List
from pythonlangutil.overload import Overload, signature

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.data_structure.solution import Solution
from binpacking.solver.data_structure.domains import Domains


class Optimisation(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, bin_packing: BinPacking2D):
        self.bin_packing = bin_packing

    def get_instance_of_problem(self) -> BinPacking2D:
        return self.bin_packing

    @abstractmethod
    @Overload
    @signature("Solution")
    def run(self, sol: Solution) -> List[Solution]:
        pass

    @abstractmethod  # type: ignore
    @run.overload
    @signature("Domains")
    def run(self, domains: Domains) -> List[Solution]:
        pass
