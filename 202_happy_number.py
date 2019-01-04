class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.square(n)
        fast = self.square(self.square(n))
        while slow != fast:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
            
        if slow == 1:
            return True
        else:
            return False
        
    def square(self, n):
        ans = 0
        while n > 0:
            ans += (n % 10) * (n % 10)
            n //= 10
        
        return ans
