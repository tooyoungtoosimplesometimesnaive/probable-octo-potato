class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        num_set = set()
        def is_square_num(n):
            if n in num_set:
                return True
            k = int(math.sqrt(n))
            if k*k == n:
                num_set.add(n)
                return True
            return False

        i = 0
        while i * i <= c:
            num_set.add(i * i)
            if is_square_num(c - i * i):
                return True
            i += 1
    
        return False

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start = 0
        end = int(math.sqrt(c))
        while start <= end:
            if start * start + end * end < c:
                start += 1
            elif start * start + end * end > c:
                end -= 1
            else:
                return True
        return False
            
