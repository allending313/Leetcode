class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        res = []

        # for digit in digits:
        #     if not res:
        #         res.extend(d[digit])
        #         continue
        #     temp = []
        #     for x in res:
        #         for y in d[digit]:
        #             temp.append(x + y)
        #     res = temp

        if not digits:
            return []

        def backtrack(curr, remaining):
            if not remaining:
                res.append(curr)
                return
            for x in d[remaining[0]]:
                backtrack(curr + x, remaining[1:])
        
        backtrack("", digits)
        return res