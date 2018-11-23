class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        result = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            tmp = divisor
            r = 1
            while dividend >= (tmp << 1):
                tmp = tmp << 1
                r = r << 1
            
            dividend -= tmp
            result += r

        if is_negative:
            result = -result

        # result should be in range [-2147483648, 2147483647]
        return min(max(-2147483648, result), 2147483647)

