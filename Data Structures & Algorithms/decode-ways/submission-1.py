class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }

        for i in range(len(s) - 1, 0 - 1, -1):
            dp[i] = dp[i + 1]

            if s[i] == "0":
                dp[i] = 0
            elif i + 2 <= len(s) and ((s[i] == "1" and s[i + 1] in "1234567890")\
                or (s[i] == "2" and s[i + 1] in "1234560")):
                dp[i] += dp[i + 2]
        
        return dp[0]