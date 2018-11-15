class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i, p in enumerate(prices):
            if i == 0:
                continue
            if prices[i - 1] < p:
                result += p - prices[i - 1]
        
        return result

