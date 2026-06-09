class Solution:
    def isAlNum(self, c):
        return ord('a') <= ord(c) <= ord('z') or\
            ord('A') <= ord(c) <= ord('Z') or\
            ord('0') <= ord(c) <= ord('9')

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlNum(s[l]):
                l += 1
            while l < r and not self.isAlNum(s[r]):
                r -= 1
            if s[l].upper() != s[r].upper():
                print(s[l], s[r], l, r)
                return False
            # print(l, r)
            l += 1
            r -= 1
        return True