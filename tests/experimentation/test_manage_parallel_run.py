from statistics import mean
from tests.base import BaseTestCase

from experimentation.manage_parallel_run import ManageParallelRun


class ManageParallelRunTest(BaseTestCase):
    @staticmethod
    def sum(n: int) -> float:
        return float(n * (n + 1)) / 2

    def test_run_parallel(self) -> None:
        r = ManageParallelRun.run_parallel(ManageParallelRunTest.sum, [3, 4, 5], ret=True)
        self.assertEqual(
            mean(r),
            mean(
                [
                    ManageParallelRunTest.sum(3),
                    ManageParallelRunTest.sum(4),
                    ManageParallelRunTest.sum(5),
                ]
            ),
        )

    def test_run_worker(self) -> None:
        r = ManageParallelRun.run_worker('echo "test"')
        self.assertEqual(r[0], 0)
        self.assertEqual(r[1], 'test')

        r = ManageParallelRun.run_worker('!echo "test"')
        self.assertEqual(r[0], 127)
