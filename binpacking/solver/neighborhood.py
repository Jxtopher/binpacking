from random import randint, random
import copy

from binpacking.solver.solution import Solution, Coordinate
from binpacking.solver.bin_packing_2d import BinPacking2D


class Neighborhood:
    def __init__(self, instance: BinPacking2D):
        self.instance = instance

    def find_random_neighbor(self, sol: Solution) -> Solution:
        s = copy.deepcopy(sol)
        for i in range(len(s)):
            capacity = self.instance.get_capacity()
            item = self.instance.get_item(i)
            if random() < 0.5:
                x, y = (
                    randint(0, capacity.width - item.width),
                    randint(0, capacity.height - item.height),
                )
                s[i] = Coordinate(x, y)
                if random() < 0.5:
                    s[i].rotate()
            else:
                s.set_coordinate_as_invalid(i)
        return s

    def find_one_mutation_neighbor(self, sol: Solution) -> Solution:
        s = copy.deepcopy(sol)
        index = randint(0, len(s)-1)
        
        if random() < 0.5:
            capacity = self.instance.get_capacity()
            item = self.instance.get_item(index)
            x, y = (
                randint(0, capacity.width - item.width),
                randint(0, capacity.height - item.height),
            )
            s[index] = Coordinate(x, y)
            if random() < 0.5:
                s[index].rotate()
        else:
            s.set_coordinate_as_invalid(index)

        return s
