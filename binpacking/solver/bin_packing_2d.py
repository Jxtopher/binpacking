from typing import List

from binpacking.types import CoordinateType
from binpacking.solver.solution import Solution


class BinPacking2D:
    def __init__(self, capacity: CoordinateType, items: List[CoordinateType]):
        self._capacity = capacity
        self._items = items

    # collision between sqaure a and b
    def collision(self, sol: Solution, a: int, b: int) -> bool:
        X: int = 0
        Y: int = 1

        if sol[b][X] - sol[a][X] < 0:
            tmp = a
            a = b
            b = tmp

        if sol[a][2] != 90:
            Ax1 = self._items[a][0]
            Ay1 = self._items[a][0]
        else:
            Ax1 = self._items[a][1]
            Ay1 = self._items[a][1]

        if sol[b][X] - sol[a][X] < Ax1 and sol[b][Y] - sol[a][Y] < Ay1:
            return True

        return False

    # def collision(self, sol: Solution, a : int, b : int) -> bool:

    #     X : int = 0
    #     Y : int = 1

    #     if sol[a][2] != 90:
    #         Ax1 = self._items[a][0]
    #         Ay1 = self._items[a][0]
    #     else:
    #         Ax1 = self._items[a][1]
    #         Ay1 = self._items[a][1]

    #     if sol[b][2] != 90:
    #         Bx1 = self._items[a][0]
    #         By1 = self._items[a][0]
    #     else:
    #         Bx1 = self._items[a][1]
    #         By1 = self._items[a][1]

    #     a = sol[a][X]
    #     b = sol[a][Y]
    #     c = sol[a][X] + Ax1
    #     d = sol[a][Y]
    #     e = sol[a][X]
    #     f = sol[a][Y] + Ay1
    #     g = sol[a][X] + Ax1
    #     h = sol[a][Y] + Ay1

    #     i = sol[b][X]
    #     j = sol[b][Y]
    #     k = sol[b][X] + Bx1
    #     l = sol[b][Y]
    #     m = sol[b][X]
    #     n = sol[b][Y] + By1
    #     o = sol[b][X] + Bx1
    #     p = sol[b][Y] + By1

    #     if a < i and i < g and b < j and j < h and g < o and h < p:
    #         return True
    #     elif a < o and o < g and b < p and p < h and a < i and j < b:
    #         return True
    #     elif e < m and m < c and d < n and n < f and c < k and l < d:
    #         return True
    #     elif e < k and k < c and d < l and l < f and m < e and f < n:
    #         return True
    #     else:
    #         return False

    def outside(self, sol: Solution, a: int) -> bool:
        X: int = 0
        Y: int = 1

        if sol[a][2] != 90:
            Ax1 = sol[a][X] + self._items[a][0]
            Ay1 = sol[a][Y] + self._items[a][0]
        else:
            Ax1 = sol[a][X] + self._items[a][1]
            Ay1 = sol[a][Y] + self._items[a][1]
        if (
            0 <= sol[a][X]
            and Ax1 <= self._capacity[X]
            and 0 <= sol[a][Y]
            and Ay1 <= self._capacity[Y]
        ):
            return False
        else:
            return True

    def evaluation(self, sol: Solution) -> None:
        # Chercher l'ensemble des objets en collision
        nbCollision: float = 0.0
        for i in range(len(sol)):
            for j in range(i + 1, len(sol)):
                if sol[i] is not None and sol[j] is not None:
                    if self.collision(sol, i, j):
                        nbCollision -= 1

        # Chercher l'ensemble des objets qui depasse de la boîte
        nbOutside: float = 0
        for i in range(len(sol)):
            if sol[i] is not None:
                if self.outside(sol, i):
                    nbOutside -= 1

        if nbCollision < 0:
            sol.set_fitness(nbCollision + nbOutside)
            return None

        #
        nbSquareValide: float = 0.0
        for i in range(len(sol)):
            if sol[i] is not None:
                nbSquareValide += 1

        sol.set_fitness(nbSquareValide)

    def get_capacity(self) -> CoordinateType:
        return self._capacity

    def get_item(self, index: int) -> CoordinateType:
        return self._items[index]

    def get_instance_size(self) -> int:
        return len(self._items)
