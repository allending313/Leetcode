class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # potions.append(0)
        # potions = sorted(potions)
        # res = []

        # for spell in spells:
        #     x, y = 0, len(potions) - 1
        #     while x <= y:
        #         m = (x + y) // 2
        #         if potions[m] * spell >= success:
        #             if potions[m - 1] * spell < success:
        #                 m = m - 1
        #                 break
        #             y = m - 1
        #         else:
        #             x = m + 1
        #     res.append(len(potions) - 1 - m)
        
        # return res

        potions.sort()
        res = []
        l = len(potions)

        for s in spells:
            n = success // s + bool(success % s)
            # res.append(l - bisect_left(potions, n))
            x, y = 0, l - 1
            while x <= y:
                m = (x + y) // 2
                if potions[m] >= n:
                    y = m - 1
                    m = y
                else:
                    x = m + 1
            
            res.append(l - 1 - m)

        return res