from random import uniform

from binpacking.solver.solution import Solution
from binpacking.solver.binPacking2D import BinPacking2D


class Neighbor:
    def __init__(self, instance: BinPacking2D):
        self.instance = instance

    def random(self, sol: Solution) -> Solution:
        s = sol
        for i in range(len(s)):
            capacity = self.instance.get_capacity()
            item = self.instance.get_item(i)
            s[i] = (
                uniform(0, capacity[0] - item[0]),
                uniform(0, capacity[1] - item[0]),
            )
        return s
