class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        res = []
        dic = defaultdict(list)
        for word in words:
            dic[word[0]].append(word[1:])
        
        m = len(board)
        n = len(board[0])
        
        def dfs(x, y, m, n, have, target, seen, res):
            cord = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen.add((x, y))
            for c in cord:
                i = x + c[0]
                j = y + c[1]
                if i >= 0 and i < m and j >= 0 and j < n and (i, j) not in seen:
                    if board[i][j] == target[0]:
                        if len(target) > 1:
                            dfs(i, j, m, n, have + board[i][j], target[1:], seen, res)
                        else:
                            res.append(have + board[i][j])
            
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in dic:
                    for x in dic[board[i][j]]:
                        if x == '':
                            res.append(board[i][j])
                        else:
                            dfs(i, j, m, n, board[i][j], x, set(), res)      
        
        return list(set(res))