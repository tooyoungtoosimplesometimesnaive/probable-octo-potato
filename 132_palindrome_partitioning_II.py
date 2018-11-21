# TLE Wrong answer:
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0
        # min_cut[i] from 0 to i, the min cut number
        min_cut = [i for i in range(len(s))]
        
        for i in range(len(s)):
            if self.is_palindrome(s[:i + 1]):
                min_cut[i] = 0
                continue
            for j in range(i + 1): # j -> 0..i
                # print(s[j:i + 1])
                if self.is_palindrome(s[j:i + 1]):
                    min_cut[i] = min(min_cut[i], min_cut[j - 1] + 1)
        
        return min_cut[-1]
    
    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# Correct answers:
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0

        p = self.get_palindrom(s)
        # print(p)
        # min_cut[i] from 0 to i, the min cut number
        min_cut = [i for i in range(len(s))]

        for i in range(len(s)):
            if p[0][i]:
                min_cut[i] = 0
                continue
            for j in range(i + 1): # j -> 0..i
                # print(s[j:i + 1])
                if p[j][i]:
                    min_cut[i] = min(min_cut[i], min_cut[j - 1] + 1)

        return min_cut[-1]

    def get_palindrom(self, s):
        p = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            p[i][i] = True
        # p[i][j] = p[i + 1][j - 1] if s[i] == s[j]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    p[i][j] = True
                elif j == i + 1:
                    p[i][j] = s[i] == s[j]
                else:
                    p[i][j] = p[i + 1][j - 1] if s[i] == s[j] else False

        return p

