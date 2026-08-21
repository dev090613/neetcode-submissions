class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):

            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i : j + 1]):
                    cur.append(s[i : j + 1])
                    dfs(j + 1, cur)
                    cur.pop()
            
            return 
        
        dfs(0, [])
        return res