from typing import Tuple, List

from binpacking.solver.solution import Solution

Coordinate = Tuple[int, int]

class BinPacking2D:
    def __init__(self, capacity : Tuple, items: List[Coordinate]):
        self._capacity = capacity
        self._list = items
    
    def evaluation(self, sol : Solution) -> None:
        #TODO calcul la qualité de la solution
        sol.set_fitness(11.5)
    
    def get_capacity(self) -> Tuple:
        return self._capacity

    def get_item(self, index : int) -> Tuple:
        return self._list[index]