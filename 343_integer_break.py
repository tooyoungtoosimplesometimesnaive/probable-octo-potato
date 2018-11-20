class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n -> no larger than 58
        product = [0] * (n + 1)
        product[1] = 1
        product[2] = 1
        
        # product[n] = max(product[k] * (n - k))
        for i in range(3, n + 1):
            for k in range(1, i):
                product[i] = max(product[i], product[k] * (i - k), k * (i - k))
        return product[-1]
        

