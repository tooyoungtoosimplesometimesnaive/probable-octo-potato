class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ways[i] : s[0, i], total number of ways
        # ways[i] = ways[i - 1] if s[i] is 1-9
        #         = ways[i - 2] if s[i-1, i] is 10 - 26
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
        if s[0] == '0':
            return 0
        ways = [0] * len(s)
        ways[0] = 1
        if s[1] == '0':
            ways[1] = 0 if int(s[:2]) > 26 else 1
        elif int(s[:2]) <= 26:
            ways[1] = 2
        else:
            ways[1] = 1

        for i in range(2, len(s)):
            n = int(s[i-1:i + 1])
            if n == 0: # 00
                ways[i] = 0
            elif s[i] == '0':
                # exclude #30
                ways[i] = 0 if n > 26 else ways[i - 2]
            elif n <= 26 and n >= 10:
                # xx
                ways[i] = ways[i - 1] + ways[i - 2]
            else:
                # 0x
                ways[i] = ways[i - 1]
        
        return ways[-1]

