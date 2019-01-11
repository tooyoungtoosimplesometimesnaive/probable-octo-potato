class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        up = 0
        down = 0
        
        for i in range(1, len(A)):
            if (down > 0 and A[i] > A[i - 1]) or A[i] == A[i - 1]:
                down = 0
                up = 0
            if A[i] > A[i - 1]:
                up += 1
            if A[i] < A[i - 1]:
                down += 1
            
            if down > 0 and up > 0:
                result = max(result, down + up + 1)
        
        return result

