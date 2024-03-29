from tests.base import BaseTestCase
from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.data_structure.solution import Solution, Coordinate


class BinPacking2DTest(BaseTestCase):
    def test_has_collision(self) -> None:
        item_a = Rectangle(6, 6)
        item_b = Rectangle(2, 2)
        instance = BinPacking2D(Rectangle(10, 10), [item_a, item_b])
        sol = Solution(instance.get_instance_size())
        self.assertTrue(instance.has_collision(sol[0], item_a, sol[1], item_b))

        sol[0] = Coordinate(4, 4)
        sol[1] = Coordinate(2, 2)
        self.assertFalse(instance.has_collision(sol[0], item_a, sol[1], item_b))

        sol[0] = Coordinate(4, 4)
        sol[1] = Coordinate(4, 4)
        self.assertTrue(instance.has_collision(sol[0], item_a, sol[1], item_b))

        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(6, 6)
        self.assertFalse(instance.has_collision(sol[0], item_a, sol[1], item_b))

        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(0, 6)
        self.assertFalse(instance.has_collision(sol[0], item_a, sol[1], item_b))

        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(5, 2)
        self.assertTrue(instance.has_collision(sol[0], item_a, sol[1], item_b))

        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(2, 5)
        self.assertTrue(instance.has_collision(sol[0], item_a, sol[1], item_b))

        sol[0] = Coordinate(2, 0)
        sol[1] = Coordinate(1, 2)
        self.assertTrue(instance.has_collision(sol[0], item_a, sol[1], item_b))

        sol[0] = Coordinate(2, 0)
        sol[1] = Coordinate(0, 2)
        self.assertFalse(instance.has_collision(sol[1], item_b, sol[0], item_a))

        sol[0] = Coordinate(2, 0)
        sol[1] = Coordinate(0, 2)
        self.assertFalse(instance.has_collision(sol[0], item_a, sol[1], item_b))

        # Rotation test
        item_a = Rectangle(6, 2)
        item_b = Rectangle(6, 2)
        instance = BinPacking2D(Rectangle(10, 10), [item_a, item_b])
        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(0, 2)
        sol[0].rotate()
        self.assertTrue(instance.has_collision(sol[0], item_a, sol[1], item_b))

    def test_has_collision_with_overlapping_rectangles(self) -> None:
        item_a = Rectangle(6, 2)
        item_b = Rectangle(2, 6)
        instance = BinPacking2D(Rectangle(10, 10), [item_a, item_b])
        sol = Solution(instance.get_instance_size())

        sol[0] = Coordinate(2, 3)
        sol[1] = Coordinate(4, 1)

        self.assertTrue(instance.has_collision(sol[0], item_a, sol[1], item_b))
        self.assertTrue(instance.has_collision(sol[1], item_b, sol[0], item_a))

        item_a = Rectangle(2, 4)
        item_b = Rectangle(4, 2)
        instance = BinPacking2D(Rectangle(10, 10), [item_a, item_b])
        sol[0] = Coordinate(2, 2)
        sol[1] = Coordinate(1, 3)
        self.assertTrue(instance.has_collision(sol[0], item_a, sol[1], item_b))
        self.assertTrue(instance.has_collision(sol[1], item_a, sol[0], item_b))

    def test_is_inside(self) -> None:
        item_0 = Rectangle(6, 6)
        instance = BinPacking2D(Rectangle(100, 100), [item_0])
        sol = Solution(instance.get_instance_size())

        sol[0] = Coordinate(0, 0)
        self.assertTrue(instance.is_inside(sol[0], item_0))

        sol[0] = Coordinate(100, 0)
        self.assertFalse(instance.is_inside(sol[0], item_0))

        sol[0] = Coordinate(99, 99)
        self.assertFalse(instance.is_inside(sol[0], item_0))

        sol[0] = Coordinate(93, 93)
        self.assertTrue(instance.is_inside(sol[0], item_0))

        # Rotation test
        item_a = Rectangle(6, 2)
        item_b = Rectangle(6, 2)
        instance = BinPacking2D(Rectangle(6, 4), [item_a, item_b])
        sol = Solution(instance.get_instance_size())
        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(0, 2)
        sol[0].rotate()
        self.assertFalse(instance.is_inside(sol[0], item_a))
        self.assertTrue(instance.is_inside(sol[1], item_b))

    def test_evaluate(self) -> None:
        ###################
        instance = BinPacking2D(
            Rectangle(100, 100),
            [Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1), Rectangle(1, 1)],
        )
        sol = Solution(instance.get_instance_size())
        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(1, 1)
        sol[2] = Coordinate(2, 2)
        sol[3] = Coordinate(3, 3)

        instance.evaluate(sol)
        fitness = sol.get_fitness()

        self.assertEqual(fitness, 4.0)

        ###################
        instance = BinPacking2D(
            Rectangle(100, 100),
            [
                Rectangle(30, 40),
                Rectangle(70, 30),
                Rectangle(30, 30),
                Rectangle(40, 70),
                Rectangle(30, 20),
                Rectangle(30, 70),
            ],
        )
        sol = Solution(instance.get_instance_size())
        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(0, 70)
        sol[2] = Coordinate(0, 40)
        sol[3] = Coordinate(30, 0)
        sol[4] = Coordinate(70, 0)
        sol[5] = Coordinate(70, 30)

        instance.evaluate(sol)
        fitness = sol.get_fitness()
        self.assertEqual(fitness, 6.0)

        ###################
        sol[0] = Coordinate(0, 0)
        sol[1] = Coordinate(0, 40)
        sol[2] = Coordinate(0, 70)
        sol[3] = Coordinate(30, 0)
        sol[3].rotate()
        sol[4] = Coordinate(30, 70)
        sol[5] = Coordinate(30, 93)
        sol[5].rotate()
        instance.evaluate(sol)
        fitness = sol.get_fitness()
        self.assertEqual(fitness, -1.0)
