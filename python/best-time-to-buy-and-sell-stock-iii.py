class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        # Tracks maximum profit/balance state after each transaction step
        first_buy = -prices[0]
        first_sell = 0
        second_buy = -prices[0]
        second_sell = 0
        
        for price in prices:
            # Maximise cash after buying the first stock
            first_buy = max(first_buy, -price)
            # Maximise cash after selling the first stock
            first_sell = max(first_sell, first_buy + price)
            # Maximise cash after buying the second stock
            second_buy = max(second_buy, first_sell - price)
            # Maximise cash after selling the second stock
            second_sell = max(second_sell, second_buy + price)
            
        return second_sell
