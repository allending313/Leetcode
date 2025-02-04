class Solution:
    def maxArea(self, height: List[int]) -> int:
        x, y, m = 0, len(height) - 1, 0

        while x < y:
            m = max(m, min(height[x], height[y]) * (y - x))
            if height[x] < height[y]:
                x += 1
            else:
                y -= 1
        return m