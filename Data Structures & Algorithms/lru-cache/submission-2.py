class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_front(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head 
        self.head.next = node


class LRUCache:

    def __init__(self, capacity: int):
        # initialize a hashmap
        # intialize a linkedlist

        # essentially, you would add nodes to the hashmap with key as key
        # then you would add it as the head to the linkedlist 
        # whenever you access through get, you get the node through the 
        # hashmap, then move it to the front of the linkedlist

        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.ll = LL()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.ll.remove(self.cache[key])
        self.ll.add_to_front(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # create a Node and add to front of the LL and add to cache
            self.cache[key] = Node(key, value)
            self.ll.add_to_front(self.cache[key])
            self.size += 1

            if self.size > self.capacity:
                del self.cache[self.ll.tail.prev.key]
                self.ll.remove(self.ll.tail.prev)
                self.size -= 1
        
        self.cache[key].value = value
        self.ll.remove(self.cache[key])
        self.ll.add_to_front(self.cache[key])
