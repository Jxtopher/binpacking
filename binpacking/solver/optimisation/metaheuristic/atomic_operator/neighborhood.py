from typing import List
from random import randint, random  # , sample

from binpacking.solver.data_structure.solution import Solution, Coordinate
from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.optimisation.optimisation import Optimisation


class Neighborhood_one_mutation(Optimisation):
    def __init__(self, bin_packing: BinPacking2D):
        self.bin_packing = bin_packing

    def run(self, sol: Solution) -> List[Solution]:
        index = randint(0, len(sol) - 1)
        capacity = self.bin_packing.get_capacity()
        item = self.bin_packing.get_item(index)
        capacity_width, capacity_height = capacity.get_width_height()
        width, height = item.get_width_height(sol[index].is_rotated)
        print(str(capacity_width - width) + " " + str(capacity_width) + " " + str(width))
        x, y = (
            randint(0, capacity_width - width),
            randint(0, capacity_height - height),
        )
        sol[index] = Coordinate(x, y)
        if random() < 0.5:
            sol[index].rotate()

        return []

    # @classmethod
    # def find_random_neighbor(cls, instance: BinPacking2D, sol: Solution) -> None:
    #     for i in range(len(sol)):
    #         if random() < 0.5:
    #             cls._set_random_coordinate(sol, i, instance)
    #         else:
    #             sol.set_coordinate_as_invalid(i)

    # @classmethod
    # def find_one_mutation_neighbor(cls, instance: BinPacking2D, sol: Solution) -> None:
    #     index = randint(0, len(sol) - 1)

    #     if random() < 0.5:
    #         cls._set_random_coordinate(sol, index, instance)
    #     else:
    #         sol.set_coordinate_as_invalid(index)

    # @classmethod
    # def find_two_mutation_neighbor(cls, instance: BinPacking2D, sol: Solution) -> None:
    #     indexes_sample = sample(range(len(sol)), 2)

    #     for index in indexes_sample:
    #         if random() < 0.5:
    #             cls._set_random_coordinate(sol, index, instance)
    #         else:
    #             sol.set_coordinate_as_invalid(index)
