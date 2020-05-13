from typing import Any, Dict
from random import randint

if __name__ == '__main__':
    instance_size = randint(0, 100)
    instance: Dict[str, Any] = {}
    instance["instance_number"] = instance_size
    instance["capcity"] = [randint(0, 100), randint(0, 100)]
    instance["items"] = [[randint(0, 10) for i in range(3)] for i in range(instance_size)]
    print(instance)
