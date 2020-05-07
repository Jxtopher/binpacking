import copy
from random import randint
from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.optimisation_algo import OptimisationAlgo
from binpacking.plot.plot_handler import PlotHandler


class Backtracking(OptimisationAlgo):
    def __init__(self, bin_packing: BinPacking2D):
        self.bin_packing = bin_packing

    def run(self, sol: Solution) -> Solution:
        self.backtracking(sol)
        return sol

    def backtracking(self, sol: Solution, number_of_valid_items: int = 0) -> Solution:
        for x in range(0, self.bin_packing.capacity.get_width_height()[0]):
            for y in range(0, self.bin_packing.capacity.get_width_height()[1]):
                for r in [0, 90]:
                    sol[number_of_valid_items] = Coordinate(x, y)
                    if r == 90:
                        sol[number_of_valid_items].rotate()
                    self.bin_packing.evaluate(sol)
                    if number_of_valid_items < len(sol) - 1:
                        if 0 <= sol.get_fitness():
                            self.backtracking(copy.deepcopy(sol), number_of_valid_items + 1)
                    else:
                        if sol.get_fitness() == len(sol):
                            print(sol)
                            plot_handler = PlotHandler(self.bin_packing, sol)
                            plot_handler.save_to_file(
                                'test_backtracking' + str(randint(0, 1000000000)) + '.png'
                            )
