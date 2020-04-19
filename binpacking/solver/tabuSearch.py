from typing import Deque
from collections import deque

from binpacking.solver.binPacking2D import BinPacking2D
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

    def run(self, sol: Solution) -> None:
        # Best known solution
        s_star = sol
        if not s_star.get_fitness_is_valid():
            self.bin_packing.evaluation(s_star)

        iterations = 0
        # while the stop criteria isn't reached
        while iterations < self.max_iterations:
            s_prim = self.neighbor.random(s_star)
            print(s_prim)
            # cpt = 0
            # while s_prim in self.taboo_list:
            #     s_prim = self.neighbor(s_star)
            #     print(s_prim)
            #     if 500 < cpt:
            #         print(cpt)
            #         raise Exception ("[-] plus de voisin trouver")
            #     cpt += 1

            self.bin_packing.evaluation(s_prim)

            # mimi ou maximi
            if s_star.get_fitness() < s_prim.get_fitness():
                s_star = s_prim

            self.taboo_list.append(s_prim)

            iterations += 1

        # s*
        # Take a non-taboo neighbor solution
        # Evaluate solution s'
        # Take best solution s* < s' : s* = s'
        # Set taboo as the considered solution s'
