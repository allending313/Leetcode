class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
        
        # x = 0
        # m = defaultdict(int)
        # res = 1

        # for y in range(len(s)):
        #     m[s[y]] += 1

        #     if y - x + 1 - max(m.values()) > k:
        #         m[s[x]] -= 1
        #         x += 1
        #     res = max(res, y - x + 1)

        # return res