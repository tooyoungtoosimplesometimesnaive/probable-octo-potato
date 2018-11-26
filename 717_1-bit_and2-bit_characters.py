class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # dp[i] from i to n - 1, if the last bit is a one-bit char
        # dp[i] = dp[i + 1] if bits[i] == 0
        #       = dp[i + 2] if bits[i] == 1
        
        if len(bits) == 0:
            return False
        if len(bits) == 1:
            return True
        
        dp = [0] * len(bits)
        dp[-1] = True
        dp[-2] = bits[-2] == 0
        
        for i in range(len(bits) - 3, -1, -1):
            dp[i] = dp[i + 2] if bits[i] == 1 else dp[i + 1]
        
        return dp[0]

