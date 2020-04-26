from typing import cast
from os import path
import json

from binpacking.types import InstanceType
from binpacking.solver.bin_packing_2d import BinPacking2D, Rectangle


class InstanceLoader:
    INSTANCES_FOLDER_NAME = 'instances'

    @classmethod
    def load_json(cls, filename: str) -> InstanceType:
        file_path = path.join(cls.INSTANCES_FOLDER_NAME, filename)
        with open(file_path) as f:
            content = f.read()
            return cast(InstanceType, json.loads(content))

    @classmethod
    def get_bin_packing(cls, file_path: str) -> BinPacking2D:
        loaded_instance = cls.load_json(file_path)
        # not super nice to cast but JSON doesn't have tuples
        capacity = Rectangle(*loaded_instance['capacity'])
        items = [Rectangle(*item) for item in loaded_instance['items']]
        b = BinPacking2D(capacity, items)
        return b
