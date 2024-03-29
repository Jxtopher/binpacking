from tests.base import BaseTestCase
from binpacking.solver.stop_criteria import StopCriteria, CriterionBudget
from binpacking.solver.data_structure.solution import Solution


class StopCriteriaTest(BaseTestCase):
    def test_run(self) -> None:
        sol = Solution(0)
        budget = CriterionBudget(50)
        stop_criteria = StopCriteria()
        stop_criteria.add_criterion(budget)

        for i in range(50):
            self.assertTrue(stop_criteria.run(sol))

        self.assertFalse(stop_criteria.run(sol))
