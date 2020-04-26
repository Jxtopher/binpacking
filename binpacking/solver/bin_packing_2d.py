from typing import List

from binpacking.types import CoordinateType
from binpacking.solver.solution import Solution


class BinPacking2D:
    def __init__(self, capacity: CoordinateType, items: List[CoordinateType]):
        self.capacity = capacity
        self.items = items

    def get_capacity(self) -> CoordinateType:
        return self.capacity

    def get_item(self, index: int) -> CoordinateType:
        return self.items[index]

    def get_instance_size(self) -> int:
        return len(self.items)

    def has_collision(self, sol: Solution, a: int, b: int) -> bool:
        return False

    def is_inside(self, sol: Solution, a: int) -> bool:
        coordinate = sol[a]
        x: int = 0
        y: int = 1

        item_position = 0 if coordinate[2] != 90 else 1
        ax1 = coordinate[x] + self.items[a][item_position]
        ay1 = coordinate[y] + self.items[a][item_position]

        return (
            0 <= coordinate[x]
            and ax1 <= self.capacity[x]
            and 0 <= coordinate[y]
            and ay1 <= self.capacity[y]
        )

    def find_num_collisions(self, sol: Solution) -> int:
        num_collisions: int = 0
        sol_length: int = len(sol)
        for i in range(sol_length):
            for j in range(i + 1, sol_length):
                if sol.is_valid_coordinate(i) and sol.is_valid_coordinate(j):
                    if self.has_collision(sol, i, j):
                        num_collisions += 1
        return num_collisions

    def evaluate(self, sol: Solution) -> None:
        num_collisions = self.find_num_collisions(sol)
        num_outside = sum(
            sol.is_valid_coordinate(i) and not self.is_inside(sol, i) for i in range(len(sol))
        )

        if num_collisions > 0:
            sol.set_fitness(-float(num_collisions + num_outside))
        else:
            num_valid_coordinates = sum(sol.is_valid_coordinate(i) for i in range(len(sol)))
            sol.set_fitness(float(num_valid_coordinates))
