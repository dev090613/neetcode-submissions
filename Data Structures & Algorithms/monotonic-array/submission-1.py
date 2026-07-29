class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pos, neg = 0, 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                pos += 1
            elif nums[i] - nums[i - 1] < 0:
                neg += 1
        
        return True if not pos or not neg else False