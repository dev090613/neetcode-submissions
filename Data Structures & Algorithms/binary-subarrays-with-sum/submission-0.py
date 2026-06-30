class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(goal):
            if goal < 0:
                return 0
            l = 0
            total = 0
            res = 0
            for r in range(len(nums)):
                total += nums[r]
                
                while total > goal:
                    total -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res
        
        return helper(goal) - helper(goal - 1)