class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup_map = {}

        for i in range(len(nums)):
            if nums[i] in dup_map:
                srt = dup_map[nums[i]]
                end = i
                if k >= (end - srt):
                    return True
            dup_map[nums[i]] = i
        return False