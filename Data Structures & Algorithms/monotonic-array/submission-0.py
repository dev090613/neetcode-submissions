class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        지속적으로 양수인가?, 지속적으로 음수인가? 를 어떻게 유지할까?
        """
        if len(nums) <= 1:
            return True
        
        pos, neg = 0, 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                pos += 1
            elif nums[i] - nums[i - 1] < 0:
                neg += 1
        
        if not neg:
            return True
        elif not pos:
            return True
        else:
            return False
