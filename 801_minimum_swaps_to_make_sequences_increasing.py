class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        swap = [float('inf') for _ in range(n)]
        keep = [float('inf') for _ in range(n)]
        
        swap[0] = 1
        keep[0] = 0
        
        for i in range(1, n):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
        
        return min(swap[n - 1], keep[n - 1])

