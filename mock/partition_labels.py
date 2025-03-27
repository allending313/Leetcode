class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        ################
        # sliding window
        ################

        dic = defaultdict(int)
        for i, c in enumerate(s):
            dic[c] = i
        
        x, y = 0, 0
        res = []

        for i, c in enumerate(s):
            y = max(y, dic[c])

            if i == y:
                res.append(y - x + 1)
                x = i + 1
    
        return res
