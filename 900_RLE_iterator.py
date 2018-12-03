class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.count_index = 0
        self.num_index = 1

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.count_index >= len(self.A) - 1:
            return -1
        
        if n == 0:
            return self.A[self.count_index + 1]
        
        while self.count_index < len(self.A) and self.A[self.count_index] < n:
            n -= self.A[self.count_index]
            self.count_index += 2

        if self.count_index < len(self.A) - 1:
            self.A[self.count_index] -= n
            return self.A[self.count_index + 1]
        else:
            return -1
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

