class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1, count_s2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord('a')
            count_s1[idx1] += 1

            idx2 = ord(s2[i]) - ord('a')
            count_s2[idx2] += 1

        matches = 0
        for i in range(26):
            matches += 1 if count_s1[i] == count_s2[i] else 0

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[i]) - ord('a')
            count_s2[idx] += 1
            if count_s2[idx] == count_s1[idx]:
                matches += 1
            elif count_s2[idx] - 1 == count_s1[idx]:
                matches -= 1

            idx = ord(s2[i - len(s1)]) - ord('a')
            count_s2[idx] -= 1
            if count_s2[idx] == count_s1[idx]:
                matches += 1
            elif count_s2[idx] + 1 == count_s1[idx]:
                matches -= 1

        return matches == 26