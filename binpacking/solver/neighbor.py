from random import randint

from binpacking.solver.solution import Solution
from binpacking.solver.binPacking2D import BinPacking2D

class Neighbor:
    def __init__(self, instance : BinPacking2D):
        self.instance = instance
    
    def random(self, sol : Solution) -> Solution:
        s = sol
        for i in range(len(s)):
            s[i] = (randint(0, self.instance.get_capacity()[0] - self.instance.get_item(i)[0]), randint(0, self.instance.get_capacity()[1]- self.instance.get_item(i)[0]))
        return s
        