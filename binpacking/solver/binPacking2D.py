from typing import Tuple, List

from binpacking.solver.solution import Solution

class BinPacking2D:
    def __init__(self, capacity : Tuple, items: List[Tuple[float, float]]):
        self._capacity = capacity
        self._list = list
    
    def evaluation(self, sol : Solution) -> None:
        #TODO calcul la qualité de la solution
        sol.set_fitness(11.5)