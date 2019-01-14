# A TLE in python but accepted in JAVA ON^2
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        i = 0
        j = 0
        start = 0
        min_len = float('inf')
        result = ""
        while i < len(S):
            if S[i] == T[0] and j == 0:
                start = i

            if S[i] == T[j]:
                if j == len(T) - 1:
                    j = 0
                    if i - start + 1 < min_len:
                        min_len = i - start + 1
                        result = S[start: i + 1]
                    i = start
                else:
                    j += 1
            
            i += 1
            
        return result

# DP Solution:

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        """
        dp[i][j] = min starting index for S[0..i] matching T[0..j]
        """
        dp = [[-1 for i in range(len(T))] for j in range(len(S))]

        for i in range(len(S)):
            dp[i][0] = i if S[i] == T[0] else -1

        for j in range(1, len(T)):
            k = -1
            for i in range(len(S)):
                if S[i] == T[j]:
                    dp[i][j] = k
                else:
                    dp[i][j] = -1
                k = max(k, dp[i][j - 1])

        result = ""
        length = float('inf')
        for i in range(len(S)):
            if dp[i][len(T) - 1] != -1:
                if i - dp[i][len(T) - 1] + 1 < length:
                    length = i - dp[i][len(T) - 1] + 1
                    result = S[dp[i][len(T) - 1]:i + 1]

        return result

