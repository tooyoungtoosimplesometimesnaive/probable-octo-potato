class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # dp[i][j] = ending with A[i] and B[j] then maximum length of subarray
        
        dp = [[0 for _ in range(len(B))] for _ in range(len(A))]
        result = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
        
        return result

