class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.m = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.m:
            # move the value
            n = self.m[key]
            self.__remove(n)
            self.__add(n)
            return n.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.m:
            self.__remove(self.m[key])

        n = Node(key, value)
        self.m[key] = n
        self.__add(n)
        if len(self.m) > self.cap:
            h = self.head.next
            self.__remove(h)
            self.m.pop(h.key)
        
    def __remove(self, n):
        # remove the node
        n_prev = n.prev
        n_next = n.next
        n_prev.next = n_next
        n_next.prev = n_prev
        
        
    def __add(self, n):
        # add the node to the end
        last = self.tail.prev
        last.next = n
        n.prev = last
        self.tail.prev = n
        n.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
