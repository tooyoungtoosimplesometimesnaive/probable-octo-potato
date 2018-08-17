class Solution:
    s = set([0, 1, 8])
    s_bad = set([3, 4, 7])
        
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        for i in range(1, N + 1):
            if self.is_good(i):
                #print(i)
                result += 1
        return result

    def is_good(self, n):
        count = 0
        length = 0
        while n >= 1:
            r = n % 10
            length += 1
            if r in self.s_bad:
                return False
            elif r in self.s:
                count += 1
            n //= 10

        return length != count

