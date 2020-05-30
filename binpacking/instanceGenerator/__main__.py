from typing import Any, Dict
from random import randint

if __name__ == '__main__':
    instance_size = randint(2, 100)
    instance: Dict[str, Any] = {}
    instance["instance_number"] = instance_size
    instance["capacity"] = [randint(1, 100), randint(1, 100)]
    instance["items"] = [[randint(1, 10) for i in range(2)] for i in range(instance_size)]
    print(instance)
