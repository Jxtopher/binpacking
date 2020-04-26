from typing import List

from binpacking.solver.solution import Solution, Coordinate


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


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
        angles_a = [
            (coordinate_a.x, coordinate_a.y),
            (coordinate_a.x + item_a.width, coordinate_a.y),
            (coordinate_a.x, coordinate_a.y + item_a.height),
            (coordinate_a.x + item_a.width, coordinate_a.y + item_a.height),
        ]
        angles_b = [
            (coordinate_b.x, coordinate_b.y),
            (coordinate_b.x + item_b.width, coordinate_b.y),
            (coordinate_b.x, coordinate_b.y + item_b.height),
            (coordinate_b.x + item_b.width, coordinate_b.y + item_b.height),
        ]

        if angles_a[1][0] <= angles_b[0][0]:  # Right
            return False
        elif angles_b[1][0] <= angles_a[0][0]:  # Left
            return False
        elif angles_a[3][1] <= angles_b[1][1]:  # Top
            return False
        elif angles_b[3][1] <= angles_a[1][1]:  # Below
            return False
        elif angles_b[1][0] <= angles_a[0][0] and angles_a[3][1] <= angles_b[1][1]:  # Right-up
            return False
        elif angles_a[3][1] <= angles_b[1][1] and angles_b[1][0] <= angles_a[0][0]:  # Top Left
            return False
        elif angles_b[3][1] <= angles_a[1][1] and angles_b[1][0] <= angles_a[0][0]:  # Below Left
            return False
        elif angles_b[3][1] <= angles_a[1][1] and angles_a[1][0] <= angles_b[0][0]:  # Below right
            return False
        return True

    def is_inside(self, coordinate: Coordinate, item: Rectangle) -> bool:
        return (
            0 <= coordinate.x
            and coordinate.x + item.width <= self.capacity.width
            and 0 <= coordinate.y
            and coordinate.y + item.height <= self.capacity.height
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

        if num_collisions > 0:
            sol.set_fitness(-float(num_collisions + num_outside))
        else:
            num_valid_coordinates = sum(coordinate.is_valid() for coordinate in sol)
            sol.set_fitness(float(num_valid_coordinates))
