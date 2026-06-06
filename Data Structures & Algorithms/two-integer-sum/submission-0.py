class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_diff = {}
        for i, n in enumerate(nums):
            diff = target - n
            
            if (diff in hash_diff):
                return [hash_diff[diff], i]
            
            hash_diff[n] = i
        