class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x, y = 0, len(numbers) - 1
        while x < y:
            if (s := numbers[x] + numbers[y]) > target:
                y -= 1
            elif s < target:
                x += 1
            else:
                return [x+1, y+1]