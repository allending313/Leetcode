class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # intuition: use a monotonic increasing stack
        # shortest bar is the limiting factor for area
        # keep track of the next shortest bar using the stack

        # keep adding bars to the stack if they are taller
        # pop bars when a shorter bar is encountered:
        # right bounds = curr index
        # left bounds = index of new top of stack or start if empty

        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            current_height = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > current_height:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area