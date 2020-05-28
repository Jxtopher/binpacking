from typing import Set, Dict, Optional
from binpacking.solver.bin_packing_2d import BinPacking2D
from binpacking.solver.solution import Coordinate


class DomainsType(Dict[int, Set[Coordinate]]):
    def __init__(
        self, bin_packing: Optional[BinPacking2D] = None, accept_invalid_coordinates: bool = True
    ) -> None:
        if bin_packing is not None:
            width, height = bin_packing.capacity.get_width_height()
            super().__init__(
                {
                    i: set(
                        Coordinate(x, y, rotation == 90)
                        for rotation in (0, 90)
                        for x in range(width)
                        for y in range(height)
                    )
                    for i in range(bin_packing.get_instance_size())
                }
            )
            if accept_invalid_coordinates:
                for i in range(bin_packing.get_instance_size()):
                    self[i].add(Coordinate(*Coordinate.INVALID_COORDINATE))
