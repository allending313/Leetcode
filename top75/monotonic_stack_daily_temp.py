class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # s = []
        # res = [0] * len(temperatures)

        # for i, x in enumerate(temperatures):
        #     if not s or x <= s[-1][1]:
        #         s.append((i, x))
        #         continue
            
        #     while s and s[-1][1] < x:
        #         j, _ = s.pop()
        #         res[j] = i - j
            
        #     s.append((i, x))
        
        # return res

        s = []
        res = [0] * len(temperatures)

        for i, x in enumerate(temperatures):
            while s and temperatures[s[-1]] < x:
                j = s.pop()
                res[j] = i - j
            s.append(i)
        
        return res