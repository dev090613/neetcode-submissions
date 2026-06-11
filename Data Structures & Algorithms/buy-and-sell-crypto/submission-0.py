class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = max(prices)
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - buy
            max_profit = max(max_profit, profit)
            if buy > prices[i]:
                buy = prices[i]
        
        return max_profit