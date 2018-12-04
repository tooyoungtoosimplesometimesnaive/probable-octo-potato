class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if len(seats) == 0:
            return 0

        left = -1
        max_dist = 0
        
        for i in range(len(seats)):
            if seats[i] == 0:
                continue
            
            if left == -1:
                max_dist = max(max_dist, i)
            else:
                max_dist = max(max_dist, (i - left) // 2)
            left = i
        
        if seats[-1] == 0:
            max_dist = max(max_dist, len(seats) - 1 - left)
        
        return max_dist

