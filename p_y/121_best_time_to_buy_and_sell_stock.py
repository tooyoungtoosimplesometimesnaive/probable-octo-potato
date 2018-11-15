class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        buy = prices[0]
        sell = 0
        for p in prices:
            buy = min(buy, p)
            sell = max(sell, p - buy)
        
        return sell

