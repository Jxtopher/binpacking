# from random import randint, random
import random

from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.bin_packing_2d import BinPacking2D


class Neighborhood:
    @staticmethod
    def find_random_neighbor(instance: BinPacking2D, sol: Solution) -> None:
        for i in range(len(sol)):
            capacity = instance.get_capacity()
            item = instance.get_item(i)
            if random.random() < 0.5:
                x, y = (
                    random.randint(0, capacity.width - item.width),
                    random.randint(0, capacity.height - item.height),
                )
                sol[i] = Coordinate(x, y)
                if random.random() < 0.5:
                    sol[i].rotate()
            else:
                sol.set_coordinate_as_invalid(i)

    @staticmethod
    def find_one_mutation_neighbor(instance: BinPacking2D, sol: Solution) -> None:
        index = random.randint(0, len(sol))

        capacity = instance.get_capacity()
        item = instance.get_item(index)
        x, y = (
            random.randint(0, capacity.width - item.width),
            random.randint(0, capacity.height - item.height),
        )
        sol[index] = Coordinate(x, y)
        if random.random() < 0.5:
            sol[index].rotate()

    @staticmethod
    def find_two_mutation_neighbor(instance: BinPacking2D, sol: Solution) -> None:
        index = random.sample(set(range(len(sol) - 1)), 2)

        capacity = instance.get_capacity()
        item = instance.get_item(index[0])
        x, y = (
            random.randint(0, capacity.width - item.width),
            random.randint(0, capacity.height - item.height),
        )
        sol[index[0]] = Coordinate(x, y)
        if random.random() < 0.5:
            sol[index[0]].rotate()

        item = instance.get_item(index[1])
        x, y = (
            random.randint(0, capacity.width - item.width),
            random.randint(0, capacity.height - item.height),
        )
        sol[index[1]] = Coordinate(x, y)
        if random.random() < 0.5:
            sol[index[1]].rotate()
