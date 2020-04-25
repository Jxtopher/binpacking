from typing import Deque
from collections import deque
import copy

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution
from binpacking.solver.neighbor import Neighbor


class TabuSearch:
    def __init__(
        self,
        bin_packing: BinPacking2D,
        taboo_list_size: int,
        max_iterations: int,
        neighbor: Neighbor,
    ):
        self.bin_packing = bin_packing
        self.taboo_list_size = taboo_list_size
        self.max_iterations = max_iterations
        self.neighbor = neighbor
        self.taboo_list: Deque[Solution] = deque(maxlen=self.taboo_list_size)

    def run(self, sol: Solution) -> Solution:
        # Best known solution
        s_star = copy.deepcopy(sol)
        if not s_star.get_fitness_is_valid():
            self.bin_packing.evaluation(s_star)

        iterations = 0
        # while the stop criteria isn't reached
        while iterations < self.max_iterations:
            s_prim = self.neighbor.random(s_star)

            # cpt = 0
            # while s_prim in self.taboo_list:
            #     s_prim = self.neighbor(s_star)
            #     print(s_prim)
            #     if 500 < cpt:
            #         print(cpt)
            #         raise Exception('[-] no more found neighbors')
            #     cpt += 1

            self.bin_packing.evaluation(s_prim)
            print(s_prim)
            # mimi ou maximi
            if s_star.get_fitness() < s_prim.get_fitness():
                s_star = copy.deepcopy(s_prim)

            self.taboo_list.append(s_prim)

            iterations += 1
        return s_star
