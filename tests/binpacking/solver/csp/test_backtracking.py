from tests.base import BaseTestCase

from binpacking.solver.statistics import Statistics
from binpacking.solver.stop_criteria import StopCriteria
from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.csp.backtracking import Backtracking
from binpacking.solver.domains import Domains


class BacktrackingTest(BaseTestCase):
    def test_backtracking(self) -> None:
        instance = BinPacking2D(
            Rectangle(2, 2), [Rectangle(2, 1), Rectangle(1, 1), Rectangle(1, 1)],
        )

        domains = Domains(instance)

        statistics = Statistics()
        stop_criteria = StopCriteria()

        backtracking = Backtracking(instance, statistics, stop_criteria)
        valid_solutions = backtracking.run(domains)

        self.assertEqual(len(valid_solutions), 49)

        for valid_solution in valid_solutions:
            instance.evaluate(valid_solution)
            self.assertTrue(valid_solution.get_fitness() >= 0)

        self.assertTrue(
            any(
                valid_solution.get_fitness() == instance.get_instance_size()
                for valid_solution in valid_solutions
            )
        )

        number_of_solutions = 0
        for valid_solution in valid_solutions:
            if valid_solution.get_fitness() == instance.get_instance_size():
                number_of_solutions += 1
        self.assertEqual(number_of_solutions, 8)

    def test_backtracking_with_stack(self) -> None:
        instance = BinPacking2D(
            Rectangle(2, 2), [Rectangle(2, 1), Rectangle(1, 1), Rectangle(1, 1)],
        )

        domains = Domains(instance)

        statistics = Statistics()
        stop_criteria = StopCriteria()

        backtracking = Backtracking(instance, statistics, stop_criteria)
        valid_solutions = backtracking.run_with_stack(domains)

        for valid_solution in valid_solutions:
            instance.evaluate(valid_solution)
            self.assertTrue(valid_solution.get_fitness() >= 0)

        number_of_solutions = sum(
            valid_solution.get_fitness() == instance.get_instance_size()
            for valid_solution in valid_solutions
        )
        self.assertEqual(number_of_solutions, 8)
