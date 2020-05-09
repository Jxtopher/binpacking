from typing import List, Optional


class Coordinate:
    INVALID_COORDINATE = (-1, -1)

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.is_rotated = False

    def __repr__(self) -> str:
        return f'({self.x}, {self.y}, {90 if self.is_rotated else 0})'

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, Coordinate)
        return self.x == other.x and self.y == other.y and self.is_rotated == other.is_rotated

    def is_valid(self) -> bool:
        return (self.x, self.y) != self.INVALID_COORDINATE

    def invalidate(self) -> None:
        self.is_rotated = False
        self.x, self.y = self.INVALID_COORDINATE

    def rotate(self, is_rotated: bool = True) -> None:
        self.is_rotated = not self.is_rotated

    def set_is_rotated(self, is_rotated: bool) -> None:
        self.is_rotated = is_rotated


class Solution(List[Coordinate]):
    def __init__(self, size: int, initial_value: Optional[Coordinate] = None):
        self.fitness_is_valid = False
        self.fitness: Optional[float] = None

        if initial_value is None:
            initial_value = Coordinate(*Coordinate.INVALID_COORDINATE)
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
        self[index].invalidate()
