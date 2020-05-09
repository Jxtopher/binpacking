from typing import List
import copy

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.optimisation_algo import OptimisationAlgo


class Backtracking(OptimisationAlgo):
    def __init__(self, bin_packing: BinPacking2D):
        self.bin_packing = bin_packing

    def run(self, sol: Solution) -> List[Solution]:
        return self.backtracking(sol)

    def backtracking(self, sol: Solution, number_of_valid_items: int = 0) -> List[Solution]:
        width, height = self.bin_packing.capacity.get_width_height()
        valid_solutions: List[Solution] = []
        for x in range(width):
            for y in range(height):
                for r in [0, 90]:
                    sol[number_of_valid_items] = Coordinate(x, y)
                    sol[number_of_valid_items].set_is_rotated(r == 90)
                    self.bin_packing.evaluate(sol)
                    if number_of_valid_items < len(sol) - 1:
                        if 0 <= sol.get_fitness():
                            valid_solutions.extend(
                                self.backtracking(copy.deepcopy(sol), number_of_valid_items + 1)
                            )
                    elif sol.get_fitness() == len(sol):
                        valid_solutions.append(copy.deepcopy(sol))
        return valid_solutions
