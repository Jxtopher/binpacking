from typing import List, Tuple, Any
from os import path
from random import uniform

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from binpacking.types import CoordinateType


class PlotHandler:
    DEFAULT_RESULTS_PATH = path.join('binpacking', 'plot', 'results')

    BACKGROUND_COLOR = '#AAAAAA'

    def __init__(
        self, capacity: CoordinateType, items: List[Tuple[CoordinateType, CoordinateType]]
    ):
        self.capacity = capacity
        self.items = items

    @staticmethod
    def _get_random_color() -> Tuple[float, float, float]:
        return (uniform(0, 1), uniform(0, 1), uniform(0, 1))

    def _process(self) -> Any:
        figure = plt.figure()
        ax = figure.add_subplot(111, aspect='equal')

        capacity_x1 = self.capacity[0]
        capacity_y1 = self.capacity[1]
        capacity_width = capacity_x1 - 0
        capacity_height = capacity_y1 - 0

        plt.xlim((0, capacity_x1))
        plt.ylim((0, capacity_y1))

        ax.add_patch(
            patches.Rectangle((0, 0), capacity_width, capacity_height, color=self.BACKGROUND_COLOR)
        )

        for item in self.items:
            (x0, y0), (x1, y1) = item
            width = x1 - x0
            height = y1 - y0
            ax.add_patch(
                patches.Rectangle(
                    (x0, y0), width, height, linewidth=1, color=self._get_random_color()
                )
            )

        return figure

    def save_to_file(self, filename: str, results_path: str = DEFAULT_RESULTS_PATH) -> str:
        figure = self._process()
        results_filepath = path.join(results_path, filename)
        figure.savefig(results_filepath, dpi=90, bbox_inches='tight')
        return results_filepath
