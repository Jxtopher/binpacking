from typing import List, Tuple

from binpacking.solver.solution import Solution, Coordinate


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def get_width_height(self, is_rotated: bool = False) -> Tuple[int, int]:
        return (self._height, self._width) if is_rotated else (self._width, self._height)


class BinPacking2D:
    def __init__(self, capacity: Rectangle, items: List[Rectangle]):
        self.capacity = capacity
        self.items = items

    def get_capacity(self) -> Rectangle:
        return self.capacity

    def get_item(self, index: int) -> Rectangle:
        return self.items[index]

    def get_instance_size(self) -> int:
        return len(self.items)

    def has_collision(
        self,
        coordinate_a: Coordinate,
        item_a: Rectangle,
        coordinate_b: Coordinate,
        item_b: Rectangle,
    ) -> bool:
        width_a, height_a = item_a.get_width_height(coordinate_a.is_rotated)
        width_b, height_b = item_b.get_width_height(coordinate_b.is_rotated)
        is_not_colliding = (
            coordinate_a.x + width_a <= coordinate_b.x
            or coordinate_b.x + width_b <= coordinate_a.x
            or coordinate_a.y + height_a <= coordinate_b.y
            or coordinate_b.y + height_b <= coordinate_a.y
        )
        return not is_not_colliding

    def is_inside(self, coordinate: Coordinate, item: Rectangle) -> bool:
        capacity_width, capacity_height = self.capacity.get_width_height()
        width, height = item.get_width_height(coordinate.is_rotated)
        return (
            0 <= coordinate.x
            and coordinate.x + width <= capacity_width
            and 0 <= coordinate.y
            and coordinate.y + height <= capacity_height
        )

    def find_num_collisions(self, sol: Solution) -> int:
        num_collisions: int = 0
        for i, coordinate_a in enumerate(sol[:-1]):  # comparing all coordinates except last ...
            opposite_coordinates = sol[i + 1 :]  # ... to the next one(s) in the list
            for j, coordinate_b in enumerate(opposite_coordinates, start=1):
                if coordinate_a.is_valid() and coordinate_b.is_valid():
                    if self.has_collision(
                        coordinate_a, self.get_item(i), coordinate_b, self.get_item(i + j)
                    ):
                        num_collisions += 1
        return num_collisions

    def evaluate(self, sol: Solution) -> None:
        num_collisions = self.find_num_collisions(sol)
        num_outside = sum(
            coordinate.is_valid() and not self.is_inside(coordinate, self.get_item(i))
            for i, coordinate in enumerate(sol)
        )

        if num_collisions > 0 or num_outside > 0:
            sol.set_fitness(-float(num_collisions + num_outside))
        else:
            num_valid_coordinates = sum(coordinate.is_valid() for coordinate in sol)
            sol.set_fitness(float(num_valid_coordinates))

    def get_available_area(self, sol: Solution) -> float:
        # TODO need to complete
        return 0.0
