class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # m = len(board)
        # n = len(board[0])
        
        # res = 0
        # seen = set()
        # coord = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # def findShip(x, y):
        #     for i, j in coord:
        #         x = x + i
        #         y = y + j
        #         if x < 0 or x >= m or y < 0 or y >= n:
        #             continue
        #         if (x, y) not in seen and board[x][y] == 'X':
        #             seen.add((x, y))
        #             findShip(x, y)
                    
        
        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) in seen:
        #             continue
        #         seen.add((i, j))
        #         if board[i][j] == 'X':
        #             res += 1
        #             findShip(i, j)
        
        # return res

        res = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                        res += 1
        
        return res