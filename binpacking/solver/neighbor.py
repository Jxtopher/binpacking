from random import randint

from binpacking.solver.solution import Solution

class Neighbor:
    @staticmethod
    def random(sol : Solution) -> Solution:
        s = sol
        for i in range(len(s)):
            s[i] = (randint(0, 1), randint(0, 1))
        return s
        