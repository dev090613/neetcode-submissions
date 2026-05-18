class Solution:
    def isPalindrome(self, s: str) -> bool:

        def helper(c):
            ascii = ord(c)
            return ord('a') <= ascii <= ord('z') or ord('A') <= ascii <= ord('Z') or ord('0') <= ascii <= ord('9')
                
        l, r = 0, len(s) - 1
        # print(s[0].lower())
        while l <= r:
            while l <= r and not helper(s[l]):
                l += 1
            while l <= r and not helper(s[r]):
                r -= 1
            
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True