class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.id = 0 # a unique id for every element

        self.stack = []
        self.heappool = []
        
        self.heap_delete = set()
        self.stack_delete = set()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        heapq.heappush(self.heappool, (-x, -self.id))
        self.stack.append((self.id, x))
        self.id += 1
        

    def pop(self):
        """
        :rtype: int
        """
        x = self.top()
        self.heap_delete.add(self.stack[-1][0])
        self.stack.pop()

        return x
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1

        while self.stack[-1][0] in self.stack_delete:
            self.stack_delete.remove(self.stack[-1][0])
            self.stack.pop()
        return self.stack[-1][1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        while -self.heappool[0][1] in self.heap_delete:
            self.heap_delete.remove(-self.heappool[0][1])
            heapq.heappop(self.heappool)
        return -self.heappool[0][0]
        

    def popMax(self):
        """
        :rtype: int
        """
        x = self.peekMax()
        _, idx = heapq.heappop(self.heappool)
        self.stack_delete.add(-idx)
        return x
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
