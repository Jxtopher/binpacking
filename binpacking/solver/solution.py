from typing import List, Optional
from copy import copy, deepcopy

from binpacking.types import CoordinateSolutionType

class Solution(List[CoordinateSolutionType]):
    def __init__(self, size: int, initial_value: CoordinateSolutionType = (0, 0, 0)):
        self._fitness_is_valid = False
        self._fitness: Optional[float] = None
        for _ in range(size):
            self.append(initial_value)

    # def __init__(self, size: int, lxx : List[CoordinateSolutionType], fitness_is_valid, fitness):
    #     self._fitness_is_valid = fitness_is_valid
    #     self._fitness: Optional[float] = fitness


    # def __deepcopy__(self, memo):
    #     # print(len(self))
    #     return Solution(5)

    # def __deepcopy__(self, memo):
    #     cls = self.__class__
    #     result = cls.__new__(cls)
    #     return result

    def get_fitness_is_valid(self) -> bool:
        return self._fitness_is_valid

    def set_fitness(self, value: float) -> None:
        self._fitness = value
        self._fitness_is_valid = True

    def get_fitness(self) -> float:
        if not self._fitness_is_valid:
            raise Exception('[-] Solution is not evaluated')
        assert isinstance(self._fitness, float)
        return self._fitness

    def __str__(self):
        tmp = ""
        for i in range(len(self)):
            tmp += str(self[i]) + ", "
        if self.get_fitness_is_valid():
            return str(self.get_fitness()) + " : [" + tmp + "]"
        else:
            return str(None) + " : [" + tmp + "]"