class LRUCache:

    # def __init__(self, capacity: int):
    #     self.m = {}         # hashmap ok {key: [value, instance]}
    #     self.q = {}         # {instance: key}
    #     self.cap = capacity # max capacity
    #     self.i = -1          # current instance counter

    # def get(self, key: int) -> int:
    #     if key in self.m:
    #         self.q.pop(self.m[key][1])
    #         self.i += 1
    #         self.m[key][1] = self.i
    #         self.q[self.i] = key
    #         return self.m[key][0]

    #     return -1

    # def put(self, key: int, value: int) -> None:
    #     if key in self.m:
    #         self.m[key][0] = value
    #         self.q.pop(self.m[key][1])
    #         self.i += 1
    #         self.m[key][1] = self.i
    #         self.q[self.i] = key
    #         return
        
    #     # key does not exist
    #     self.i += 1
    #     self.m[key] = [value, self.i]
    #     self.q[self.i] = key

    #     # over capacity
    #     if len(self.q) > self.cap:
    #         k = min(self.q)
    #         self.m.pop(self.q[k])
    #         self.q.pop(k)
    #     return

# class LinkedNode:
#     def __init__(self, key = -1, val = -1):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = dict()
#         self.head = LinkedNode()
#         self.tail = LinkedNode()
#         self.head.next = self.tail
#         self.tail.prev = self.head
        
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
        
#         node = self.__evict(key)
#         self.__addToEnd(node)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.__delete(key)

#         node = LinkedNode(key, value)
#         self.cache[key] = node
#         self.__addToEnd(node)
        
#         if len(self.cache) > self.capacity:
#             self.__delete(self.head.next.key)
    
#     def __evict(self, key) -> LinkedNode: 
#         node = self.cache[key]
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         node.next = None
#         node.prev = None
#         return node

#     def __delete(self, key) -> None:
#         deleteNode = self.__evict(key)
#         del deleteNode
#         del self.cache[key]

#     def __addToEnd(self, node) -> None:
#         node.prev = self.tail.prev
#         node.next = self.tail
#         self.tail.prev.next = node
#         self.tail.prev = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache[key] = self.cache.pop(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)