from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # print(collections.Counter(strs[0]))

        hash_map = defaultdict(list)
        # print(Counter(strs[0]))
        for s in strs:
            count = collections.Counter(s)
            anagram = [0] * 26
            for k, v in count.items():
                anagram[ord(k) - ord('a')] = v
            hash_map[tuple(anagram)].append(s)
        return list(hash_map.values())