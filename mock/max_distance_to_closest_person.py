class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        lastPerson = -1
        res = 1
        n = len(seats)
        
        for i, s in enumerate(seats):
            if s:
                if lastPerson < 0:
                    res = max(res, i)
                else:
                    res = max(res, (i - lastPerson) // 2)
                lastPerson = i
        
        if not seats[i]:
            res = max(res, i - lastPerson)
        
        return res