class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = set()

        n, p, z = [], [], 0
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z += 1

        N, P = set(n), set(p)

        if z > 0:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

            if z >= 3:
                res.add((0, 0, 0))

        from itertools import combinations

        for x, y in combinations(n, 2):
            target = -(x + y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))

        for x, y in combinations(p, 2):
            target = -(x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))

        return [list(x) for x in res]