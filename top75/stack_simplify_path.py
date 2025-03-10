class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for x in path.split('/'):
            if res and x == '..':
                res.pop()
            elif x not in {'', '.', '..'}:
                res.append(x)
        
        return '/' + '/'.join(res)