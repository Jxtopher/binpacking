from typing import Set, Dict, Optional
from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Coordinate


class Domains(Dict[int, Set[Coordinate]]):
    def __init__(
        self, bin_packing: Optional[BinPacking2D] = None, accept_invalid_coordinates: bool = True
    ) -> None:
        if bin_packing is not None:
            width, height = bin_packing.capacity.get_width_height()
            super().__init__({i: set() for i in range(bin_packing.get_instance_size())})

            for i in range(bin_packing.get_instance_size()):
                item_width, item_height = bin_packing.get_item(i).get_width_height()
                for x in range(width):
                    for y in range(height):
                        if item_width != item_height:
                            for rotation in (0, 90):
                                self[i].add(Coordinate(x, y, rotation == 90))
                        else:
                            self[i].add(Coordinate(x, y))

            if accept_invalid_coordinates:
                for i in range(bin_packing.get_instance_size()):
                    self[i].add(Coordinate(*Coordinate.INVALID_COORDINATE))
