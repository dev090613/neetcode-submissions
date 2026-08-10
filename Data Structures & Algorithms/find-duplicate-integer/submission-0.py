class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bucket = [-1] * (len(nums) + 1)
        
        for n in nums:
            if bucket[n] == n:
                return n
            bucket[n] = n