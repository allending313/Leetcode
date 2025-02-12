class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # q = list(senate)
        # i = 0
        # while len(q) > 1 and i < len(q) - 1:
        #     if q[i] != q[i + 1]:
        #         q.pop(i + 1)
        #         q.append(q.pop(i))
        #         i = 0
        #     elif q[i] == q[i + 1]:
        #         i += 1
        
        # return 'Radiant' if q[0] == 'R' else 'Dire'

        r = deque()
        d = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            elif senate[i] == 'D':
                d.append(i)
        
        while len(r) > 0 and len(d) > 0:
            x = r.popleft()
            y = d.popleft()

            if x < y:
                r.append(x + n)
            elif y < x:
                d.append(y + n)
        
        return 'Radiant' if len(d) == 0 else 'Dire'
            