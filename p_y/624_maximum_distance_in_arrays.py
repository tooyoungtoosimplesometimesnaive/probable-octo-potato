class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        if len(arrays) == 0:
            return 0
        max_value = arrays[0][-1]
        min_value = arrays[0][0]
        result = 0
        for i in range(1, len(arrays)):
            result = max(result, abs(max_value - arrays[i][0]), abs(min_value - arrays[i][-1]))
            max_value = max(max_value, arrays[i][-1])
            min_value = min(min_value, arrays[i][0])
        
        
        return result

