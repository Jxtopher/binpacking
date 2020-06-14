from typing import List
from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle


class BinPacking2D_overload(BinPacking2D):
    def __init__(self, capacity: List[int], items: List[List[int]]) -> None:
        _item: List[Rectangle] = []
        for item in items:
            _item.append(Rectangle(item[0], item[1]))
        super().__init__(Rectangle(capacity[0], capacity[1]), _item)
