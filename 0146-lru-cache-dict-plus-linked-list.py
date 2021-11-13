class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
    def __str__(self):
        # For debugging
        return f"(key={self.key}, val={self.val})"
            
class LinkedList:
    def __init__(self):
        # Note: sentinel.next points to the first element or self if it's empty.
        # And sentinel.prev points to the last element, or self if it's empty.
        self.sentinel = Node(None, None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def pop(self, node: Node = None):
        if not node:
            node = self.sentinel.prev  # pop tail if no node provided
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node

    def appendleft(self, node: Node):
        if not node:
            return
        node.prev = self.sentinel
        node.next = self.sentinel.next
        node.next.prev = node
        self.sentinel.next = node

    def last(self):
        if self.sentinel.prev is not self.sentinel:
            return self.sentinel.prev
        return None

    def first(self):
        if self.sentinel.next is not self.sentinel:
            return self.sentinel.next
        return None

    def __str__(self):
        # For debugging
        s = []
        node = self.sentinel.next
        while node is not self.sentinel:
            s.append(f"({node.key},{node.val})")
            node = node.next
        return ",".join(s)

class LRUCache:
    # Initial design:
    # Use a double linked list to store the keys in order of
    # most recently used at head to least recently used at the tail.
    # When a key is queried, the node is moved to head.
    # Eject entries when adding entry but capacity is reached.

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index = dict()  # For O(1) access to nodes
        self.reverse_index = dict()  # For mapping node -> key
        self.list = LinkedList()
        

    def get(self, key: int) -> int:
        val = -1
        if key and key in self.index:
            node = self.index[key]
            self.list.pop(node)
            self.list.appendleft(node)
            val = node.val
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.index:
            self.index[key].val = value
            self.list.pop(self.index[key])
            self.list.appendleft(self.index[key])
        else:
            if len(self.index) == self.capacity:
                node = self.list.pop()
                del self.index[node.key]
            self.index[key] = Node(key, value)
            self.list.appendleft(self.index[key])
