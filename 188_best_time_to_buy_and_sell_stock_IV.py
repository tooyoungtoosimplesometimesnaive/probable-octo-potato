class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k <= 0:
            return 0
        if len(prices) <= 1:
            return 0
        
        if k >= len(prices) // 2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] - prices[i - 1] > 0:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [float('inf')] * k
        sell = [0] * k
        # buy = float('inf')
        # sell = 0
        
        for price in prices:
            # buy[0] = min(buy[0], price)
            # sell[0] = max(sell[0], price - buy[0])
            # buy[1] = min(buy[1], price - sell[0])
            # sell[1] = max(sell[1], price - buy[1])
            # buy[2] = min(buy[2], price - sell[1])
            # sell[2] = max(sell[2], price - buy[2])
            buy[0] = min(buy[0], price)
            sell[0] = max(sell[0], price - buy[0])
            for i in range(1, k):
                buy[i] = min(buy[i], price - sell[i - 1])
                sell[i] = max(sell[i], price - buy[i])
                
        return sell[-1]

