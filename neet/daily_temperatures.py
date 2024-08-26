class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing (or equal) stack
        stack = []
        res = [0] * len(temperatures)

        for i, x in enumerate(temperatures):
            while stack and stack[-1][0] < x:
                (_, j) = stack.pop()
                res[j] = i - j
            stack.append((x, i))
        
        return res