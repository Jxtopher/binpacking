from typing import List, Optional, Tuple

Coordinate = Tuple[int, int]

class Solution(List[Coordinate]):
    def __init__(self, size: int, value_initial: Coordinate = (0,0)):
        self._fitness_is_valid = False
        self._fitness : Optional[float] = None
        for _ in range(size):
            self.append(value_initial)

    def get_fitness_is_valid(self) -> bool:
        return self._fitness_is_valid

    def set_fitness(self, value: float) -> None:
        self._fitness = value
        self._fitness_is_valid = True

    def get_fitness(self) -> float:
        if not self._fitness_is_valid:
            raise Exception ("[-] Solution n'est evaluaté")
        assert isinstance(self._fitness, float)
        return self._fitness