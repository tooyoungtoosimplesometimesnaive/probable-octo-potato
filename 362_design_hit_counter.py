class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = [0 for i in range(300)]
        self.hits = [0 for i in range(300)]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        index = timestamp % 300
        if self.time[index] != timestamp:
            self.time[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        total = 0
        for i in range(300):
            if timestamp - self.time[i] < 300:
                total += self.hits[i]
        
        return total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
