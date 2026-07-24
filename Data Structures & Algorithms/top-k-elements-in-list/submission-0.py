class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        res = []
        tuples = Counter(nums).most_common(k)
        for t in tuples:
            
            res.append(t[0])
        return res
        
