from unittest import TestCase

from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution
from binpacking.plot.plot_handler import PlotHandler

class BinPacking2DTest(TestCase):
    def test_collision(self) -> None:
        instance = BinPacking2D([10,10], [[6,6], [2, 2]])
        solution = Solution(instance.get_instance_size())
        self.assertEqual(instance.collision(solution, 0, 1), True)

        solution[0] = [0,0,0]
        solution[1] = [6,6,0]
        self.assertEqual(instance.collision(solution, 0, 1), False)

        solution[0] = [0,0,0]
        solution[1] = [0,6,0]
        self.assertEqual(instance.collision(solution, 0, 1), False)

        solution[0] = [0,0,0]
        solution[1] = [5,2,0]
        self.assertEqual(instance.collision(solution, 0, 1), True)

        solution[0] = [0,0,0]
        solution[1] = [2,5,0]
        self.assertEqual(instance.collision(solution, 0, 1), True)

        solution[0] = [2,0,0]
        solution[1] = [1,2,0]
        plot_handler = PlotHandler(instance, solution)
        results_filepath = plot_handler.save_to_file('test_1.png')
        # self.assertEqual(instance.collision(solution, 0, 1), True)

        solution[0] = [2,0,0]
        solution[1] = [0,2,0]
        self.assertEqual(instance.collision(solution, 1, 0), False)

        solution[0] = [2,0,0]
        solution[1] = [0,2,0]
        self.assertEqual(instance.collision(solution, 0, 1), False)


    def test_outside(self) -> None:
        instance = BinPacking2D([100,100], [[6,6]])
        solution = Solution(instance.get_instance_size())
        solution[0] = [0,0,0]
        self.assertEqual(instance.outside(solution, 0), False)

        solution[0] = [100,0,0]
        self.assertEqual(instance.outside(solution, 0), True)


        solution[0] = [99,99,0]
        self.assertEqual(instance.outside(solution, 0), True)

        solution[0] = [93,93,0]
        self.assertEqual(instance.outside(solution, 0), False)


    def test_evaluation(self) -> None:
        instance = BinPacking2D([100,100], [[1,1], [1, 1], [1, 1], [1, 1]])
        solution = Solution(instance.get_instance_size())
        

        solution[0] = [0,0,0]
        solution[1] = [1,1,0]
        solution[2] = [2,2,0]
        solution[3] = [3,3,0]
        
        instance.evaluation(solution)
        print(solution.get_fitness())

        self.assertEqual('foo'.upper(), 'FOO')
