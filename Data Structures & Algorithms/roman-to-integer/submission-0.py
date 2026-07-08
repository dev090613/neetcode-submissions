class Solution:
    def romanToInt(self, s: str) -> int:
        
        hash_map = { "I": 1,
            "V": 5, "X": 10, "L": 50, 
            "C": 100, "D": 500, "M": 1000
            }
        res = 0
        prev = 1000000
        for i in range(len(s)):
            val = int(hash_map[s[i]])
            if val > prev:
                val -= prev
                res -= prev
            
            res += val
            prev = val
            print(val)
            
        return res