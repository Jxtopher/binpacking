from typing import List, Optional


class Coordinate:
    INVALID_COORDINATE = (-1, -1)

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self.is_rotated = False

    @property
    def x(self) -> int:
        return self._y if self.is_rotated else self._x

    @property
    def y(self) -> int:
        return self._x if self.is_rotated else self._y

    def is_valid(self) -> bool:
        return (self._x, self._y) != self.INVALID_COORDINATE

    def invalidate(self) -> None:
        self.is_rotated = False
        self._x, self._y = self.INVALID_COORDINATE

    def rotate(self) -> None:
        self.is_rotated = not self.is_rotated


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
