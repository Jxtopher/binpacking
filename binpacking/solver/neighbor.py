from random import randint, uniform
import copy

from binpacking.solver.solution import Solution
from binpacking.solver.bin_packing_2d import BinPacking2D


class Neighbor:
    def __init__(self, instance: BinPacking2D):
        self.instance = instance

    def random(self, sol: Solution) -> Solution:
        s = copy.deepcopy(sol)
        for i in range(len(s)):
            capacity = self.instance.get_capacity()
            item = self.instance.get_item(i)
            if uniform(0,1) < 0.5:
                s[i] = (
                    randint(0, capacity[0] - item[0]),  # x
                    randint(0, capacity[1] - item[0]),  # y
                    randint(0, 1) * 90,                 # Rotation
                )
            else:
                s[i] = None
        return s

    def one_case_mutation(self, sol : Solution) -> Solution:
        s = copy.deepcopy(sol)

        if uniform(0,1) < 0.5:
            s[randint(0, len(s))] = (
                    randint(0, capacity[0] - item[0]),  # x
                    randint(0, capacity[1] - item[0]),  # y
                    randint(0, 1) * 90,                 # Rotation
                )
        else:
            s[i] = None

        return s