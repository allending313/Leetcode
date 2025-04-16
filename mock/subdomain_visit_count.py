class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        for d in cpdomains:
            n, d = d.split()
            n = int(n)
            dic[d] += n
            pos = d.find('.') + 1
            
            while pos > 0:
                dic[d[pos:]] += n
                pos = d.find('.', pos) + 1
        
        res = []
        for k, v in dic.items():
            res.append(f'{v} {k}')
        
        return res