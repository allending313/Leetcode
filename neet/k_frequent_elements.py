class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [x for x,_ in c.most_common(k)]

        # c = Counter(nums)
        # buckets = [[] for _ in range(len(nums) + 1)]
        # for val, freq in c.items():
        #     buckets[freq].append(val)
        
        # res = []
        # for b in reversed(buckets):
        #     for val in b:
        #         res.append(val)
        #         k -= 1
        #         if k == 0:
        #             return res