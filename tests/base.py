from typing import Callable, Any
import os
from unittest import TestCase, skipUnless

from binpacking.plot.plot_handler import PlotHandler
from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution

from random import seed


class BaseTestCase(TestCase):
    RUN_TIME_CONSUMING_TESTS = os.environ.get('RUN_TIME_CONSUMING_TESTS') == '1'

    @classmethod
    def setUpClass(cls) -> None:
        seed(55)

    @classmethod
    def timeConsumingTest(
        cls, reason_if_skip: str = 'Time consuming tests not enabled',
    ) -> Callable[..., Any]:
        return skipUnless(cls.RUN_TIME_CONSUMING_TESTS, reason_if_skip)

    def debug_plot(
        self, instance: BinPacking2D, sol: Solution, filename: str = 'plot_test.png'
    ) -> str:
        plot_handle = PlotHandler(instance, sol)
        return plot_handle.save_to_file(filename)
