from typing import Tuple, List
import json

from binpacking.solver.binPacking2D import BinPacking2D

class InstanceLoader:
    @staticmethod 
    def loadJson(file_path : str) -> dict:
        with open(file_path) as f:
            return json.loads(f.read())

    @classmethod
    def get_bin_packing(cls, file_path: str) -> BinPacking2D :
        x = cls.loadJson(file_path)
        items = [tuple(item) for item in x['items']]
        b = BinPacking2D(tuple(x["capacity"]), items)
        return b