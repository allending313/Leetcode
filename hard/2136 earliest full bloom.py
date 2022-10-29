class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = sorted(zip(growTime, plantTime), reverse=True)
        day = res = -1
        for g, p in times:
            day += p
            res = max(res, day + g + 1)
        return res