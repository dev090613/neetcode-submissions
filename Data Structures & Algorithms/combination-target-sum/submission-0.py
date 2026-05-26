class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []
        def dfs(cur, i, total):
            if target == total:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return
                cur.append(nums[j])
                dfs(cur, j, total + nums[j])
                cur.pop()
        
        dfs([], 0, 0)
        return res