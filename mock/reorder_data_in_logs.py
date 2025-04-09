class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = defaultdict(list)
        res = []
        
        for log in logs:
            if log[-1].isalpha():
                k, v = log.split(" ", 1)
                letter[v].append(k)
            else:
                digit.append(log)
        
        for k in sorted(letter.keys()):
            v = letter[k]
            if len(v) == 1:
                res.append(v[0] + " " + k)
            else:
                for x in sorted(v):
                    res.append(x + " " + k)
        
        return res + digit