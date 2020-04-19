from typing import cast
from os import path
import json

from binpacking.types import InstanceType, CoordinateType
from binpacking.solver.bin_packing_2d import BinPacking2D


class InstanceLoader:
    INSTANCES_FOLDER_NAME = 'instances'

    @classmethod
    def loadJson(cls, filename: str) -> InstanceType:
        file_path = path.join(cls.INSTANCES_FOLDER_NAME, filename)
        with open(file_path) as f:
            content = f.read()
            return cast(InstanceType, json.loads(content))

    @classmethod
    def get_bin_packing(cls, file_path: str) -> BinPacking2D:
        loaded_instance = cls.loadJson(file_path)
        # not super nice to cast but JSON doesn't have tuples
        capacity = cast(CoordinateType, tuple(loaded_instance['capacity']))
        items = [cast(CoordinateType, tuple(item)) for item in loaded_instance['items']]
        b = BinPacking2D(capacity, items)
        return b
