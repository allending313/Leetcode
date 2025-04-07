class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # def nums(cells: List[int]) -> int:
        #     res = 0
        #     for x in cells[::-1]:
        #         res += x
        #         res *= 10
        #     return res

        # dic = defaultdict(list)
        # dic[nums(cells)] = [0]

        for x in range(n % 14 + 14):
            prev = cells[0]
            for i in range(1, 7):
                if bool(prev) ^ bool(cells[i + 1]):
                    prev = cells[i]
                    cells[i] = 0
                else:
                    prev = cells[i]
                    cells[i] = 1
            if x == 0:
                cells[0] = 0
                cells[7] = 0
            # dic[nums(cells)].append(x)
                
        
        return cells
        