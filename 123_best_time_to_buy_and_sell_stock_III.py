class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit = sell_price_1 - buy_price_1 + sell_price_2 - buy_price_2
        # buy1   = buy_price_1
        # sell1  = sell_price_1 - buy_price_1
        # buy2   = buy_price_2 - (sell_price_1 - buy_price_1)
        #        = buy_price_2 - sell_price_1 + buy_price_1
        # sell2  = sell_price_2 - buy2
        # sell2  = sell_price_2 - (buy_price_2 - sell_price_1 + buy_price_1)
        #        = sell_price_2 - buy_price_2 + sell_price_1 - buy_price_1
        buy1 = float('inf')
        buy2 = float('inf')
        sell1 = 0
        sell2 = 0
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
            print("{} {} {} {}".format(buy1, sell1, buy2, sell2))
        
        return sell2

