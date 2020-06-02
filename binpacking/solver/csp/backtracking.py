from typing import List
import copy

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.statistics import Statistics
from binpacking.solver.stop_criteria import StopCriteria
from binpacking.solver.solution import Solution
from binpacking.solver.csp.arcconsistency.ac3 import AC3
from binpacking.solver.domains import Domains


class Backtracking:
    def __init__(
        self, bin_packing: BinPacking2D, statistics: Statistics, stop_criteria: StopCriteria
    ):
        self.bin_packing = bin_packing
        self.statistics = statistics
        self.stop_criteria = stop_criteria
        self.ac3 = AC3(self.bin_packing)

    def run(self, domains: Domains) -> List[Solution]:
        valid_solutions: List[Solution] = []

        self.ac3.run(domains)

        for domain in domains.values():
            if len(domain) == 0:
                return valid_solutions  # empty

        if all(len(domain) == 1 for domain in domains.values()):
            valid_sol = Solution(len(domains))
            for i in range(len(domains)):
                valid_sol[i] = domains[i].pop()
            valid_solutions.append(valid_sol)
            return valid_solutions

        width, height = self.bin_packing.capacity.get_width_height()
        for sol_index, domain in domains.items():
            if len(domain) == 1:
                continue
            for coordinate in domain:
                domains[sol_index] = {coordinate}
                valid_solutions.extend(self.run(copy.deepcopy(domains)))
            break

        return valid_solutions
