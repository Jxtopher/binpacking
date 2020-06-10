# @bref : Iterated local search
#         Ramalhinho-Lourenço, Helena, Martin, Olivier C. and Stützle, Thomas, (2000),
#         Iterated local search, Economics Working Papers, Department of Economics and Business,
#         Universitat Pompeu Fabra, https://EconPapers.repec.org/RePEc:upf:upfgen:513.
#         (https://econ-papers.upf.edu/papers/513.pdf)

from typing import List
import copy

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.statistics import Statistics
from binpacking.solver.stop_criteria import StopCriteria
from binpacking.solver.data_structure.solution import Solution
from binpacking.solver.optimisation.optimisation import Optimisation


class IteratedLocalSearch(Optimisation):
    def __init__(
        self,
        bin_packing: BinPacking2D,
        statistics: Statistics,
        stop_criteria: StopCriteria,
        atomic_operator: Optimisation,
        optimisation: Optimisation,
    ):
        self.bin_packing = bin_packing
        self.statistics = statistics
        self.stop_criteria = stop_criteria
        self.atomic_operator = atomic_operator
        self.optimisation = optimisation

    def run(self, sol: Solution) -> List[Solution]:
        # Best known solution
        s_star = copy.deepcopy(sol)
        if not s_star.has_valid_fitness():
            self.bin_packing.evaluate(s_star)

        # while the stop criteria isn't reached
        while self.stop_criteria.run(s_star):
            s_prim = copy.deepcopy(s_star)
            self.atomic_operator.run(s_prim)
            self.optimisation.run(s_prim)

            if not s_star.has_valid_fitness():
                self.bin_packing.evaluate(s_prim)

            if s_star.get_fitness() < s_prim.get_fitness():
                s_star = copy.deepcopy(s_prim)
                to_print = self.statistics.run(s_star)
                if to_print:
                    print(to_print)

        return [s_star]
