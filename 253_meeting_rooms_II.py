# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals == None or len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x:x.start)
        result = 1
        
        pool = []
        heapq.heappush(pool, intervals[0].end)
        
        for i in range(1, len(intervals)):
            end = pool[0]
            if intervals[i].start < end:
                result += 1
            else:
                heapq.heappop(pool)
            heapq.heappush(pool, intervals[i].end)

        
        return result

