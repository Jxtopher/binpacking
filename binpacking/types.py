from typing import List, Tuple, TypedDict


CoordinateType = Tuple[int, int]
CoordinateSolutionType = Tuple[int, int, int]


class InstanceType(TypedDict):
    name: str
    instance_number: str
    capacity: List[int]
    items: List[List[int]]
