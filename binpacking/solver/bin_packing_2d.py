from typing import List

from binpacking.types import CoordinateType
from binpacking.solver.solution import Solution


class BinPacking2D:
    def __init__(self, capacity: CoordinateType, items: List[CoordinateType]):
        self._capacity = capacity
        self._items = items

    
    # collision between sqaure a and b
    def collision(self, sol: Solution, a : int, b : int) -> bool:
        print("=")
        X : int = 0
        Y : int = 1

        if sol[b][X] - sol[a][X] < 0 :
            tmp = a
            a = b
            b = tmp

        if sol[a][2] != 90:
            Ax1 = self._items[a][0]
            Ay1 = self._items[a][0]
        else:
            Ax1 = self._items[a][1]
            Ay1 = self._items[a][1]

        print(sol[b][X] - sol[a][X])
        print(sol[b][Y] - sol[a][Y])
        if sol[b][X] - sol[a][X] < Ax1 and sol[b][Y] - sol[a][Y] < Ay1:
            return True
        
        return False
    def evaluation(self, sol: Solution) -> None:
        # TOD calculate the solution quality

        sol.set_fitness(11.5)

    def get_capacity(self) -> CoordinateType:
        return self._capacity

    def get_item(self, index: int) -> CoordinateType:
        return self._items[index]

    def get_instance_size(self):
        return len(self._items)