# one last test case failed.
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        dp[i] => ways to decode s[:i]
        dp[i] = 
            last one digit:
                if s[i] == *
                    += dp[i - 1] * 9
                else if s[i] != * and s[i] != 0:
                    += dp[i - 1]
            last two digits (as a whole):
                **:
                    += 15 * dp[i - 2]
                *X:
                    if X = 1 2 3 4 5 6, += 2 * dp[i - 2]
                    if X = 7,8,9        += dp[i - 2]
                X*:
                    if X = 1            += 9 * dp[i - 2]
                    if X = 2            += 6 * dp[i - 2]
                else:
                if s[i-1: i] >=10 and <= 26: += dp[i - 2]
        """
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0

        dp = [0 for _ in range(len(s))]
        # Base case for dp[0]
        dp[0] = 9 if s[0] == '*' else 0 if s[0] == '0' else 1
        if len(s) == 1:
            return dp[0]

        # Base case for dp[1]:
        if s[:2] == '**':
            dp[1] = 96
        elif s[0] == '*':
            if s[1] == '0': dp[1] = 2
            elif int(s[1]) <= 6: dp[1] = 11
            elif int(s[1]) > 6: dp[1] = 9
        elif s[1] == '*':
            if int(s[0]) == 1: dp[1] = 18
            elif int(s[0]) == 2: dp[1] = 15
            else: dp[1] = 9
        elif s[1] == '0':
            dp[1] = 0 if int(s[:2]) > 26 else 1
        elif int(s[:2]) <= 26:
            dp[1] = 2
        else:
            dp[1] = 1
        
        for i in range(2, len(s)):
            if s[i] == '*':
                dp[i] += 9 * dp[i - 1]
            elif s[i] != '*' and s[i] != '0':
                dp[i] += dp[i - 1]
            
            if s[i - 1] == '*' and s[i] == '*':
                dp[i] += 15 * dp[i - 2]
            # *X 
            elif s[i - 1] == '*' and int(s[i]) >= 0 and int(s[i]) <= 6:
                dp[i] += 2 * dp[i - 2]
            elif s[i - 1] == '*' and int(s[i]) >= 7:
                dp[i] += dp[i - 2]
            # X*
            elif s[i] == '*' and int(s[i - 1]) == 1:
                dp[i] += 9 * dp[i - 2]
            elif s[i] == '*' and int(s[i - 1]) == 2:
                dp[i] += 6 * dp[i - 2]
            # elif s[i] == '*' and int(s[i - 1]) != 1:
            #     print('here')
            #     # No way to construct 2 digit number
            #     dp[i] += 0
            elif s[i - 1] != '*' and s[i] != '*' and int(s[i - 1: i + 1]) <= 26 and int(s[i - 1: i + 1]) >= 10:
                dp[i] += dp[i - 2]

            dp[i] = dp[i] % 1000000007
        
        return dp[-1]
        
