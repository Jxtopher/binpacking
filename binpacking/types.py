from typing import List, TypedDict


class InstanceType(TypedDict):
    name: str
    instance_number: str
    capacity: List[int]
    items: List[List[int]]
