# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        def get_start(interval):
            return interval.start
        intervals = sorted(intervals, key=get_start)
        
        result = []
        a = intervals[0]
        i = 1
        while i < len(intervals):
            b = intervals[i]
            if a.end < b.start:
                result.append(a)
                a = b
            else:
                a.end = max(a.end, b.end)
            i += 1
        result.append(a)
        return result
            
        
