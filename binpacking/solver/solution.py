from typing import List, Optional

from binpacking.types import CoordinateSolutionType


class Solution(List[CoordinateSolutionType]):
    INVALID_COORDINATE = (-1, -1, 0)

    def __init__(self, size: int, initial_value: CoordinateSolutionType = INVALID_COORDINATE):
        self._fitness_is_valid = False
        self._fitness: Optional[float] = None
        for _ in range(size):
            self.append(initial_value)

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

    def set_coordinate_as_invalid(self, index: int) -> None:
        self[index] = self.INVALID_COORDINATE

    def is_valid_coordinate(self, index: int) -> bool:
        return self[index] != self.INVALID_COORDINATE

    def __str__(self) -> str:
        tmp = ''
        for i in range(len(self)):
            tmp += str(self[i]) + ', '
        if self.get_fitness_is_valid():
            return str(self.get_fitness()) + ' : [' + tmp + ']'
        else:
            return str(None) + ' : [' + tmp + ']'
