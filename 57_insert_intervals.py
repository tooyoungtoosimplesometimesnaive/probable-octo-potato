# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]

        result = []
        already_inserted = False
        for i in intervals:
            if i.end < newInterval.start:
                result.append(i)
            elif i.start > newInterval.end:
                if not already_inserted:
                    result.append(newInterval)
                    already_inserted = True
                result.append(i)
            else:
                newInterval.start = min(newInterval.start, i.start)
                newInterval.end = max(newInterval.end, i.end)

        if not already_inserted:
            result.append(newInterval)
        return result

