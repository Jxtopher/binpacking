from random import randint, random, sample

from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.bin_packing_2d import BinPacking2D


class Neighborhood:
    @staticmethod
    def _set_random_coordinate(sol: Solution, i: int, instance: BinPacking2D) -> None:
        capacity = instance.get_capacity()
        item = instance.get_item(i)
        capacity_width, capacity_height = capacity.get_width_height()
        width, height = item.get_width_height(sol[i].is_rotated)
        x, y = (
            randint(0, capacity_width - width),
            randint(0, capacity_height - height),
        )
        sol[i] = Coordinate(x, y)
        if random() < 0.5:
            sol[i].rotate()

    @classmethod
    def find_random_neighbor(cls, instance: BinPacking2D, sol: Solution) -> None:
        for i in range(len(sol)):
            if random() < 0.5:
                cls._set_random_coordinate(sol, i, instance)
            else:
                sol.set_coordinate_as_invalid(i)

    @classmethod
    def find_one_mutation_neighbor(cls, instance: BinPacking2D, sol: Solution) -> None:
        index = randint(0, len(sol) - 1)

        if random() < 0.5:
            cls._set_random_coordinate(sol, index, instance)
        else:
            sol.set_coordinate_as_invalid(index)

    @classmethod
    def find_two_mutation_neighbor(cls, instance: BinPacking2D, sol: Solution) -> None:
        indexes_sample = sample(range(len(sol)), 2)

        for index in indexes_sample:
            if random() < 0.5:
                cls._set_random_coordinate(sol, index, instance)
            else:
                sol.set_coordinate_as_invalid(index)
