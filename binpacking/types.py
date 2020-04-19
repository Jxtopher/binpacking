from typing import List, Tuple, TypedDict


CoordinateType = Tuple[float, float]


class InstanceType(TypedDict):
    name: str
    instance_number: str
    capacity: List[float]
    items: List[List[float]]
