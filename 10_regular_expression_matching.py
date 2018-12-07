class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        dp[i][j] => first i chars of s matched first j chars of p;
        
        dp[i][j] = 
            if p[j - 1] != * and p[j - 1] != .
                s[i - 1] == p[j - 1] and dp[i - 1][j - 1]
            if p[j - 1] == .
                dp[i - 1][j - 1]
            if p[j - 1] == *
                if p[j - 2] != . and s[i - 1] != p[j - 2]
                    dp[i][j - 2]
                if p[j - 2] == s[i - 1] or p[j - 2] == .
                    dp[i][j - 2] (match 0)
                    dp[i - 1][j] (match 1)
        
        base case :
        dp[0][0] = True
        dp[0][j] = p[j - 1] == * and dp[j -2]
        dp[i][0] = False
        """
        # len(s) + 1 rows and len(p) + 1 cols
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        
        for i in range(len(s) + 1):
            dp[i][0] = False
        dp[0][0] = True
        if len(p) > 0:
            dp[0][1] = False
        for j in range(2, len(p) + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 2]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*' and p[j - 1] != '.':
                    dp[i][j] = p[j - 1] == s[i - 1] and dp[i - 1][j - 1] 
                elif p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*' and j > 1:
                    if p[j - 2] != '.' and s[i - 1] != p[j - 2]:
                        dp[i][j] = dp[i][j - 2]
                    elif p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
        
        # print(dp)
        return dp[len(s)][len(p)]

