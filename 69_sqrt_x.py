class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        start = 1
        end = x
        while start < end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid 
            elif mid * mid < x:
                start = mid + 1
            else:
                return mid
        return end - 1

