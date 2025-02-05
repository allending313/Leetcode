class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m, c = 0, 0

        for x in gain:
            c += x
            m = max(m, c)

        return m