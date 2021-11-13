from collections import OrderedDict

class LRUCache:

    # Initial design:
    # Use a linked list to store the keys in order of
    # most recently used to least recently used at the tail.
    # When a key is queried, the node is moved to head.

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        val = -1
        if key in self.dict:
            val = self.dict[key]
            self.dict.move_to_end(key, last=False)
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
        elif len(self.dict) == self.capacity:
            self.dict.popitem()
        self.dict[key] = value
        self.dict.move_to_end(key, last=False)