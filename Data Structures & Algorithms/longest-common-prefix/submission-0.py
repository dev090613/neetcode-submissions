class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        첫 번째 문자열을 기준으로 순회한다.
            문자가 
            
        """
        res = ""
        for i in range(len(strs[0])):            
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res
                