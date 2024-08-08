class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total = 0

        while left < right:
            if left_max < right_max:
                left += 1   
                left_max = max(left_max, height[left])
                total += left_max - height[left]
            else:
                right -= 1    
                right_max = max(right_max, height[right])
                total += right_max - height[right]
        
        return total
        
        
        # left_max, right_max = [], []
        # total = 0

        # for i in range(len(height)):
        #     left_max.append(max(height[i], left_max[i-1] if i != 0 else 0))

        # for i in range(len(height) - 1, -1, -1):
        #     right_max.append(max(height[i], right_max[len(height) - 2 - i] if i != len(height) - 1 else 0))

        # potential = [min(x, y) for x, y in zip(left_max, right_max[::-1])]

        # for h, p in zip(height, potential):
        #     if (v := p - h) > 0:
        #         total += v

        # return total