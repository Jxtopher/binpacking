from typing import List, Tuple, Any
from os import path
from random import uniform

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from binpacking.solver.solution import Solution
from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle


class PlotHandler:
    DEFAULT_RESULTS_PATH = path.join('binpacking', 'plot', 'results')

    BACKGROUND_COLOR = '#AAAAAA'

    def __init__(self, instance: BinPacking2D, sol: Solution):
        self.capacity = instance.get_capacity()
        self.rectangles_with_coordinates: List[Tuple[int, int, Rectangle]] = []

        for i, coordinate in enumerate(sol):
            if coordinate.is_valid():
                item = instance.get_item(i)
                self.rectangles_with_coordinates.append((coordinate.x, coordinate.y, item))

    @staticmethod
    def _get_random_color() -> Tuple[float, float, float]:
        return (uniform(0, 1), uniform(0, 1), uniform(0, 1))

    def _process(self) -> Any:
        figure = plt.figure()
        ax = figure.add_subplot(111, aspect='equal')

        plt.xlim((0, self.capacity.width))
        plt.ylim((0, self.capacity.height))

        ax.add_patch(
            patches.Rectangle(
                (0, 0), self.capacity.width, self.capacity.height, color=self.BACKGROUND_COLOR
            )
        )

        for rectangle_with_coordinate in self.rectangles_with_coordinates:
            x, y, rectangle = rectangle_with_coordinate
            ax.add_patch(
                patches.Rectangle(
                    (x, y),
                    rectangle.width,
                    rectangle.height,
                    linewidth=1,
                    color=self._get_random_color(),
                )
            )

        return figure

    def save_to_file(self, filename: str, results_path: str = DEFAULT_RESULTS_PATH) -> str:
        figure = self._process()
        results_filepath = path.join(results_path, filename)
        figure.savefig(results_filepath, dpi=90, bbox_inches='tight')
        return results_filepath
