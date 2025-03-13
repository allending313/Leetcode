class Solution:
    def hammingWeight(self, n: int) -> int:
        # poolish 20 
        # mix wet 40
        # str 1   30
        # str 2   90 
        # ball    30
        # shape   60
        # bake    30

        # 225 water  -> 450
        # 350 flour  -> 700
        # 30 poolish -> 60
        # 3 tsp salt
        # 3 tsp yeast

        res = 0
        while n:
            n &= n - 1 # clears the rightmost set bit (1)
            res += 1
        return res
