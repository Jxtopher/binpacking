from unittest import TestCase

from binpacking.plot.plot_handler import PlotHandler
from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Solution


class BaseTestCase(TestCase):
    def debug_plot(
        self, instance: BinPacking2D, sol: Solution, filename: str = 'plot_test.png'
    ) -> str:
        plot_handle = PlotHandler(instance, sol)
        return plot_handle.save_to_file(filename)
