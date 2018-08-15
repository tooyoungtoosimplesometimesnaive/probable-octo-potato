class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(A)
        cols = len(A[0])
        
        A_t = []
        for c in range(0, cols):
            A_t.append(list(map(lambda row : row[c], A)))
        
        return A_t

