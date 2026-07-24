class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket 을 생성한다.
        # nums의 각 n에 대한 개수를 센다.
        # 개수는 버킷의 인덱스가 된다. 해당 인덱스에 n을 append한다.
        # 버킷을 뒤로 루프, k 번째 존재하는 n 들을 수집하여 반환한다.

        buckets = [ [] for _ in range(len(nums) + 1) ]
        # print(buckets)

        counter = defaultdict(int)
        for i in range(len(nums)):
            counter[nums[i]] += 1
        # print(counter)

        for n, idx in counter.items():
            buckets[idx].append(n)
        
        res = []
        for l in reversed(buckets):
            if not l:
                continue
            if k == 0:
                break
            for n in l:
                res.append(n)
                k -= 1
                if k == 0:
                    break

        return res

            