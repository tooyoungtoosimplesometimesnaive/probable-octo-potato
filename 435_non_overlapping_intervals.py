# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from functools import cmp_to_key
class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals == None or len(intervals) == 0:
            return 0

        intervals.sort(key=cmp_to_key(lambda a, b: a.start - b.start if a.start != b.start else a.end - b.end ))
        
        # for a in intervals:
        #     print(a.start, a.end)

        current = intervals[0]
        result = 0
        i = 1
        while i < len(intervals):
            next_interval = intervals[i]
            if current.end > next_interval.start:
                result += 1
                if current.end > next_interval.end:
                    current.end = next_interval.end
            else:
                current = next_interval
            i += 1
        
        return result

