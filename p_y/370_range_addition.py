class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        result = [0 for _ in range(length)]
        
        for start, end, inc in updates:
            result[start] += inc
            if end + 1 < length:
                result[end + 1] -= inc
        
        for i in range(1, length):
            result[i] += result[i - 1]
        
        
        return result
    
