# @brief : F. Glover, "Future paths for integer programming and links to artificial intelligence,"
#          Computers & Operations Research, vol. 13, pp. 533-549, 1986.

from typing import Deque, Callable
from collections import deque
import copy

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution
from binpacking.solver.optimisation_algo import OptimisationAlgo


class TabuSearch(OptimisationAlgo):
    def __init__(
        self,
        bin_packing: BinPacking2D,
        tabu_size: int,
        max_iterations: int,
        find_neighborhood: Callable[[BinPacking2D, Solution], None],
    ):
        self.bin_packing = bin_packing
        self.tabu_size = tabu_size
        self.max_iterations = max_iterations
        self.find_neighborhood = find_neighborhood
        self.tabu_deque: Deque[Solution] = deque(maxlen=self.tabu_size)

    def run(self, sol: Solution) -> Solution:
        # Best known solution
        s_star = copy.deepcopy(sol)
        if not s_star.has_valid_fitness():
            self.bin_packing.evaluate(s_star)

        iterations = 0
        # while the stop criteria isn't reached
        while iterations < self.max_iterations:
            s_prim = copy.deepcopy(s_star)
            self.find_neighborhood(self.bin_packing, s_prim)

            cpt = 0
            while s_prim in self.tabu_deque:
                self.find_neighborhood(self.bin_packing, s_prim)
                if 500 < cpt:
                    raise Exception('[-] no more found neighbors')
                cpt += 1

            self.bin_packing.evaluate(s_prim)

            # mimi ou maximi
            if s_star.get_fitness() < s_prim.get_fitness():
                s_star = copy.deepcopy(s_prim)
                print(s_star)

            self.tabu_deque.append(s_prim)

            iterations += 1
        return s_star
