from typing import List

from binpacking.types import CoordinateType
from binpacking.solver.solution import Solution


class BinPacking2D:
    def __init__(self, capacity: CoordinateType, items: List[CoordinateType]):
        self._capacity = capacity
        self._items = items

    # collision between sqaure a and b
    def collision(self, sol: Solution, a: int, b: int) -> bool:
        x: int = 0
        y: int = 1

        if sol[b][x] - sol[a][x] < 0:
            a, b = b, a

        if sol[a][2] != 90:
            ax1 = self._items[a][0]
            ay1 = self._items[a][0]
        else:
            ax1 = self._items[a][1]
            ay1 = self._items[a][1]

        if sol[b][x] - sol[a][x] < ax1 and sol[b][y] - sol[a][y] < ay1:
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
        x: int = 0
        y: int = 1

        if sol[a][2] != 90:
            ax1 = sol[a][x] + self._items[a][0]
            ay1 = sol[a][y] + self._items[a][0]
        else:
            ax1 = sol[a][x] + self._items[a][1]
            ay1 = sol[a][y] + self._items[a][1]
        if (
            0 <= sol[a][x]
            and ax1 <= self._capacity[x]
            and 0 <= sol[a][y]
            and ay1 <= self._capacity[y]
        ):
            return False
        else:
            return True

    def evaluation(self, sol: Solution) -> None:
        # Find number of collisions
        num_collisions: int = 0
        for i in range(len(sol)):
            for j in range(i + 1, len(sol)):
                if sol.is_valid_coordinate(i) and sol.is_valid_coordinate(j):
                    if self.collision(sol, i, j):
                        num_collisions += 1

        # Find number of rectangles that are outside
        num_outside: int = 0
        for i in range(len(sol)):
            if sol.is_valid_coordinate(i):
                if self.outside(sol, i):
                    num_outside += 1

        if num_collisions > 0:
            sol.set_fitness(-float(num_collisions + num_outside))
        else:
            num_valid_squares: int = 0
            for i in range(len(sol)):
                if sol.is_valid_coordinate(i):
                    num_valid_squares += 1

            sol.set_fitness(float(num_valid_squares))

    def get_capacity(self) -> CoordinateType:
        return self._capacity

    def get_item(self, index: int) -> CoordinateType:
        return self._items[index]

    def get_instance_size(self) -> int:
        return len(self._items)
