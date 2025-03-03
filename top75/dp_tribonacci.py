class Solution:
    def tribonacci(self, n: int) -> int:
        # dq = deque([0, 1, 1])
        # if n < 3:
        #     return dq[n]        

        # for _ in range(n - 2):
        #     s = sum(dq)
        #     dq.append(s)
        #     dq.popleft()
        
        # return dq[-1]

        d = defaultdict(int)
        d[0], d[1], d[2] = 0, 1, 1

        for i in range(3, n + 1):
            d[i] = d[i - 1] + d[i - 2] + d[i - 3]
        
        return d[n]