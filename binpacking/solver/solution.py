from typing import List, Optional

from binpacking.types import CoordinateSolutionType


class Solution(List[CoordinateSolutionType]):
    INVALID_COORDINATE = (-1, -1, 0)

    def __init__(self, size: int, initial_value: CoordinateSolutionType = INVALID_COORDINATE):
        self.fitness_is_valid = False
        self.fitness: Optional[float] = None
        for _ in range(size):
            self.append(initial_value)

    def __str__(self) -> str:
        fitness_label = str(self.get_fitness() if self.has_valid_fitness() else None)
        return f'{fitness_label}: {super().__str__()}'

    def get_fitness(self) -> float:
        if not self.fitness_is_valid:
            raise Exception('[-] Solution is not evaluated')
        assert isinstance(self.fitness, float)
        return self.fitness

    def set_fitness(self, value: float) -> None:
        self.fitness = value
        self.fitness_is_valid = True

    def has_valid_fitness(self) -> bool:
        return self.fitness_is_valid

    def set_coordinate_as_invalid(self, index: int) -> None:
        self[index] = self.INVALID_COORDINATE

    def is_valid_coordinate(self, index: int) -> bool:
        return self[index] != self.INVALID_COORDINATE
