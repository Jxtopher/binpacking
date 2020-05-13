from random import randint, random
from typing import List
import copy

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.statistics import Statistics
from binpacking.solver.stop_criteria import StopCriteria
from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.optimisation_algo import OptimisationAlgo


class Backtracking(OptimisationAlgo):
    def __init__(
        self,
        bin_packing: BinPacking2D,
        statistics: Statistics,
        stop_criteria: StopCriteria,
        randomize: bool = False,
    ):
        self.bin_packing = bin_packing
        self.statistics = statistics
        self.stop_criteria = stop_criteria
        self.randomize = randomize

    def run(self, sol: Solution) -> List[Solution]:
        if self.randomize:
            return self.run_randomize(sol)
        else:
            return self.run_deterministic(sol)

    def run_deterministic(self, sol: Solution, number_of_valid_items: int = 0) -> List[Solution]:
        width, height = self.bin_packing.capacity.get_width_height()
        valid_solutions: List[Solution] = []
        for x in range(width):
            for y in range(height):
                for r in [0, 90]:
                    sol[number_of_valid_items] = Coordinate(x, y)
                    sol[number_of_valid_items].set_is_rotated(r == 90)
                    self.bin_packing.evaluate(sol)
                    if number_of_valid_items < len(sol) - 1 and self.stop_criteria.run(sol):
                        if 0 <= sol.get_fitness():
                            valid_solutions.extend(
                                self.run_deterministic(
                                    copy.deepcopy(sol), number_of_valid_items + 1
                                )
                            )
                    else:
                        if sol.get_fitness() == len(sol):
                            to_print = self.statistics.run(sol)
                            if to_print:
                                print(to_print)
                            valid_solutions.append(copy.deepcopy(sol))
        return valid_solutions

    def run_randomize(self, sol: Solution, number_of_valid_items: int = 0) -> List[Solution]:
        width, height = self.bin_packing.capacity.get_width_height()
        valid_solutions: List[Solution] = []

        iteration = 0
        while iteration < 10000:
            x = randint(0, width)
            y = randint(0, height)
            r = randint(0, 1)

            sol[number_of_valid_items] = Coordinate(x, y)
            sol[number_of_valid_items].set_is_rotated(bool(r))
            self.bin_packing.evaluate(sol)
            if number_of_valid_items < len(sol) - 1 and self.stop_criteria.run(sol):
                to_print = self.statistics.run(sol)
                if to_print:
                    print(to_print)
                if 0 <= sol.get_fitness():
                    valid_solutions.extend(
                        self.run_randomize(copy.deepcopy(sol), number_of_valid_items + 1)
                    )
            else:
                if sol.get_fitness() == len(sol):
                    to_print = self.statistics.run(sol)
                    if to_print:
                        print(to_print)
                    valid_solutions.append(copy.deepcopy(sol))
            iteration += 1
        return valid_solutions
