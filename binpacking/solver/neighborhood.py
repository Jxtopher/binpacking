from random import randint, random, sample

from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.bin_packing_2d import BinPacking2D


class Neighborhood:
    @staticmethod
    def find_random_neighbor(instance: BinPacking2D, sol: Solution) -> None:
        for i in range(len(sol)):
            capacity = instance.get_capacity()
            item = instance.get_item(i)
            if random() < 0.5:
                x, y = (
                    randint(0, capacity.width - item.width),
                    randint(0, capacity.height - item.height),
                )
                sol[i] = Coordinate(x, y)
                if random() < 0.5:
                    sol[i].rotate()
            else:
                sol.set_coordinate_as_invalid(i)

    @staticmethod
    def find_one_mutation_neighbor(instance: BinPacking2D, sol: Solution) -> None:
        index = randint(0, len(sol) - 1)

        if random() < 0.5:
            capacity = instance.get_capacity()
            item = instance.get_item(index)
            x, y = (
                randint(0, capacity.width - item.width),
                randint(0, capacity.height - item.height),
            )
            sol[index] = Coordinate(x, y)
            if random() < 0.5:
                sol[index].rotate()
        else:
            sol.set_coordinate_as_invalid(i)

    @staticmethod
    def find_two_mutation_neighbor(instance: BinPacking2D, sol: Solution) -> None:
        indexes_sample = sample(set(range(len(sol))), 2)

        capacity = instance.get_capacity()

        if random() < 0.5:
            for i in indexes_sample:
                item = instance.get_item(indexes_sample[i])
                x, y = (
                    randint(0, capacity.width - item.width),
                    randint(0, capacity.height - item.height),
                )
                sol[indexes_sample[i]] = Coordinate(x, y)
                if random() < 0.5:
                    sol[indexes_sample[i]].rotate()
        else:
            sol.set_coordinate_as_invalid(i)
