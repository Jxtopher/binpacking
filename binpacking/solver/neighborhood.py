from random import randint, random
import copy

from binpacking.solver.solution import Solution
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
                s[i] = (
                    randint(0, capacity[0] - item[0]),  # x
                    randint(0, capacity[1] - item[0]),  # y
                    randint(0, 1) * 90,  # Rotation
                )
            else:
                s.set_coordinate_as_invalid(i)
        return s
