class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        t = ord(target)
        x, y = 0, len(letters) - 1

        while x <= y:
            m = (x + y) // 2
            curr = ord(letters[m])
            if m - 1 >= 0 and curr > t and ord(letters[m - 1]) <= t:
                return letters[m]
            if curr > t:
                y = m - 1
            else:
                x = m + 1
        
        return letters[0]

            