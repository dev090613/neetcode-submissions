class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(remain):
            if remain == 0:
                return 0
            if remain in cache:
                return cache[remain]
            
            res = 1e9
            for c in coins:
                if remain - c >= 0:
                    res = min(res, 1 + dfs(remain - c))
            
            cache[remain] = res
            return res
        
        return dfs(amount) if dfs(amount) != 1e9 else -1