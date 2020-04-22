from typing import List

from binpacking.types import CoordinateType
from binpacking.solver.solution import Solution


class BinPacking2D:
    def __init__(self, capacity: CoordinateType, items: List[CoordinateType]):
        self._capacity = capacity
        self._items = items

    
    # collision between sqaure a and b
    def collision(self, sol: Solution, a : int, b : int) -> bool:
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

        if sol[b][X] - sol[a][X] < Ax1 and sol[b][Y] - sol[a][Y] < Ay1:
            return True
        
        return False

    def outside(self, sol : Solution, a : int) -> bool:
        X : int = 0
        Y : int = 1

        if sol[a][2] != 90:
            Ax1 = sol[a][X] + self._items[a][0]
            Ay1 = sol[a][Y] + self._items[a][0]
        else:
            Ax1 = sol[a][X] + self._items[a][1]
            Ay1 = sol[a][Y] + self._items[a][1]
        if  0 <= sol[a][X] and Ax1 <= self._capacity[X] and 0 <= sol[a][Y] and  Ay1 <= self._capacity[Y]:
            return False
        else:
            return True
    def evaluation(self, sol: Solution) -> None:
        # Chercher l'ensemble des objets en collision
        nbCollision : float = 0.0
        for i in range(len(sol)):
            for j in range(i+1, len(sol) ):
                if sol[i] != None and sol[j] != None:
                    if self.collision(sol, i, j):
                        nbCollision -= 1

        # Chercher l'ensemble des objets qui depasse de la boîte
        nbOutside : float = 0
        for i in range(len(sol)):
            if sol[i] != None:
                if self.outside(sol, i):
                    nbOutside -= 1

        if nbCollision < 0:
            sol.set_fitness(nbCollision + nbOutside)
            return None

        # 
        nbSquareValide : float = 0.0
        for i in range(len(sol)):
            if sol[i] != None:
                nbSquareValide += 1

        sol.set_fitness(nbSquareValide)

    def get_capacity(self) -> CoordinateType:
        return self._capacity

    def get_item(self, index: int) -> CoordinateType:
        return self._items[index]

    def get_instance_size(self):
        return len(self._items)