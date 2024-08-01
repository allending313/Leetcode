class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, squ = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    continue
                if v in row[i] or v in col[j] or v in squ[(i // 3, j // 3)]:
                    return False
                row[i].add(v)
                col[j].add(v)
                squ[(i // 3, j // 3)].add(v)

        return True