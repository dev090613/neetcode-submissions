class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for a in range(amount + 1):
            for c in coins:
                if a >= c:
                    dp[c] = 1
                    dp[a] = min(dp[a], dp[a - c] + dp[c])
        return dp[amount] if dp[amount] != float('inf') else -1