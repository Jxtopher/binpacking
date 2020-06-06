from tests.base import BaseTestCase
from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle
from binpacking.solver.csp.arcconsistency.ac3 import AC3
from binpacking.solver.domains import Domains


class AC3Test(BaseTestCase):
    def test_ac3_with_all_fitting_inputs(self) -> None:
        instance = BinPacking2D(
            Rectangle(100, 100), [Rectangle(10, 10), Rectangle(20, 20), Rectangle(10, 30)],
        )

        ac3 = AC3(instance)
        domains = Domains(instance)
        ac3.run(domains)
        self.assertEqual(sum(len(sub_domain) for sub_domain in domains.values()), 27767)

    def test_ac3_without_all_fitting_inputs(self) -> None:
        instance = BinPacking2D(
            Rectangle(10, 10), [Rectangle(1, 1), Rectangle(8, 8), Rectangle(3, 3)],
        )

        ac3 = AC3(instance)
        domains = Domains(instance)
        ac3.run(domains)
        self.assertEqual(sum(len(sub_domain) for sub_domain in domains.values()), 127)

    def test_ac3_with_all_fitting_inputs_2(self) -> None:
        instance = BinPacking2D(
            Rectangle(100, 100), [Rectangle(10, 10), Rectangle(20, 20), Rectangle(10, 30)],
        )

        ac3 = AC3(instance)
        domains = Domains(instance)
        ac3.run(domains)

        self.assertEqual(sum(len(sub_domain) for sub_domain in domains.values()), 27767)
