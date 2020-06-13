from tests.base import BaseTestCase

from binpacking.solver.factory import Factory


class FactoryTest(BaseTestCase):
    def test_factory_csp_backtracking(self) -> None:
        config = {
            "seed": 0,
            "dataStructure": "Domains",
            "OptimizationAlgorithm": "Backtracking",
            "Backtracking": {
                "BinPacking2D_overload": {"capacity": [2, 2], "items": [[2, 1], [1, 1], [1, 1]]},
                "Statistics": {},
                "StopCriteria": {},
            },
        }
        instance = Factory.build_config(config)
        results = Factory.run_solver(config, instance)

        self.assertEqual(len(results), 49)
        pass
