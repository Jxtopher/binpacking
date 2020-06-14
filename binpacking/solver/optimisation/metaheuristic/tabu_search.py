#
# @brief : F. Glover, "Future paths for integer programming and links to artificial intelligence,"
#          Computers & Operations Research, vol. 13, pp. 533-549, 1986.
#

from typing import Deque, List
from collections import deque
import copy

from binpacking.solver.statistics import Statistics
from binpacking.solver.stop_criteria import StopCriteria
from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.data_structure.solution import Solution
from binpacking.solver.optimisation.optimisation import Optimisation


class TabuSearch(Optimisation):
    def __init__(
        self,
        bin_packing: BinPacking2D,
        statistics: Statistics,
        stop_criteria: StopCriteria,
        tabu_size: int,
        atomic_operator: Optimisation,
    ):
        self.bin_packing = bin_packing
        self.statistics = statistics
        self.stop_criteria = stop_criteria
        self.tabu_size = tabu_size
        self.atomic_operator = atomic_operator
        self.tabu_deque: Deque[Solution] = deque(maxlen=self.tabu_size)

    def run(self, sol: Solution) -> List[Solution]:
        # Best known solution
        s_star = copy.deepcopy(sol)
        if not s_star.has_valid_fitness():
            self.bin_packing.evaluate(s_star)

        # while the stop criteria isn't reached
        while self.stop_criteria.run(s_star):
            s_prim = copy.deepcopy(s_star)
            self.atomic_operator.run(s_prim)

            cpt = 0
            while s_prim in self.tabu_deque:
                self.atomic_operator.run(s_prim)
                if 500 < cpt:
                    raise Exception('[-] no more found neighbors')
                cpt += 1

            self.bin_packing.evaluate(s_prim)

            # mimi ou maximi
            if s_star.get_fitness() < s_prim.get_fitness():
                s_star = copy.deepcopy(s_prim)
                to_print = self.statistics.run(s_star)
                if to_print:
                    print(to_print)

            self.tabu_deque.append(s_prim)

        return [s_star]
