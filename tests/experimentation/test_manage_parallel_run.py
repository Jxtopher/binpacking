from statistics import mean

from tests.base import BaseTestCase
from binpacking.experimentations.manage_parallel_run import ManageParallelRun


class ManageParallelRunTest(BaseTestCase):
    @staticmethod
    def sum_1_to_n(n: int) -> float:
        return float(n * (n + 1)) / 2

    def test_run_parallel(self) -> None:
        r = ManageParallelRun.run_parallel(ManageParallelRunTest.sum_1_to_n, [3, 4, 5], ret=True)
        self.assertEqual(
            mean(r),
            mean(
                [
                    ManageParallelRunTest.sum_1_to_n(3),
                    ManageParallelRunTest.sum_1_to_n(4),
                    ManageParallelRunTest.sum_1_to_n(5),
                ]
            ),
        )

    def test_run_worker(self) -> None:
        r = ManageParallelRun.run_worker('echo "test"')
        self.assertEqual(r[0], 0)
        self.assertEqual(r[1], 'test')

        r = ManageParallelRun.run_worker('!echo "test"')
        self.assertEqual(r[0], 127)
