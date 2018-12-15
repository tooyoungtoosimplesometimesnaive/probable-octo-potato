class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower_pool = [] # max heap
        self.higher_pool = [] # min heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.lower_pool, -num)
        
        heapq.heappush(self.higher_pool, -heapq.heappop(self.lower_pool))
        
        if len(self.higher_pool) > len(self.lower_pool):
            heapq.heappush(self.lower_pool, -heapq.heappop(self.higher_pool))

        # print(self.lower_pool)
        # print(self.higher_pool)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lower_pool) > len(self.higher_pool):
            return -self.lower_pool[0]
        else:
            return (-self.lower_pool[0] + self.higher_pool[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

