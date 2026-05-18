class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Loop (num - 1) in num_set?
            # O => not start
            # X => start
        num_set = set(nums)
        length, max_len = 0, 0
        for n in (num_set):
            if (n - 1) not in num_set:
                length = 0
                while n + length in num_set:
                    length += 1
                max_len = max(max_len, length)
        max_len = max(max_len, length)
        return max_len