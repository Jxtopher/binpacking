# @bref : Iterated local search
#         Ramalhinho-Lourenço, Helena, Martin, Olivier C. and Stützle, Thomas, (2000),
#         Iterated local search, Economics Working Papers, Department of Economics and Business,
#         Universitat Pompeu Fabra, https://EconPapers.repec.org/RePEc:upf:upfgen:513.
#         (https://econ-papers.upf.edu/papers/513.pdf)
import copy

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution
from binpacking.solver.neighborhood import Neighborhood
from binpacking.solver.optimisation_algo import OptimisationAlgo


class IteratedLocalSearch(OptimisationAlgo):
    def __init__(
        self, bin_packing: BinPacking2D, max_iterations: int, optimisation_algo: OptimisationAlgo
    ):
        self.bin_packing = bin_packing
        self.max_iterations = max_iterations
        self.optimisation_algo = optimisation_algo

    def run(self, sol: Solution) -> Solution:
        # Best known solution
        s_star = copy.deepcopy(sol)
        if not s_star.has_valid_fitness():
            self.bin_packing.evaluate(s_star)

        iterations = 0

        # while the stop criteria isn't reached
        while iterations < self.max_iterations:
            s_prim = copy.deepcopy(s_star)
            Neighborhood.find_random_neighbor(self.bin_packing, s_prim)
            self.optimisation_algo.run(s_prim)

            if not s_star.has_valid_fitness():
                self.bin_packing.evaluate(s_prim)

            if s_star.get_fitness() < s_prim.get_fitness():
                s_star = copy.deepcopy(s_prim)
                print(s_star)
            iterations += 1

        return s_star
