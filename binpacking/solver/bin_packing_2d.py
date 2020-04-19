from typing import List

from binpacking.types import CoordinateType
from binpacking.solver.solution import Solution


class BinPacking2D:
    def __init__(self, capacity: CoordinateType, items: List[CoordinateType]):
        self._capacity = capacity
        self._items = items

    def evaluation(self, sol: Solution) -> None:
        # TODO: calculate the solution quality
        sol.set_fitness(11.5)

    def get_capacity(self) -> CoordinateType:
        return self._capacity

    def get_item(self, index: int) -> CoordinateType:
        return self._items[index]
