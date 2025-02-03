class Solution:
    def compress(self, chars: List[str]) -> int:
        # prev, i = 0, 1
        # while i < len(chars):
        #     if chars[i] == chars[prev]:
        #         next = chars[prev + 1]
        #         if next.isnumeric():
        #             chars[prev + 1] = str(int(next) + 1)
        #             del chars[i]
        #             i -= 1
        #         else:
        #             chars[prev + 1] = "2"
        #     else:
        #         prev = i
        #     i += 1

        # i = 0
        # while i < len(chars):
        #     if len(chars[i]) > 1:
        #         for y in chars[i]:
        #             chars.insert(i, y)
        #             i += 1
        #         del chars[i]
        #     i += 1
        
        # return len(chars)

        i, pcount = 0, 1

        while i < len(chars):
            if i == len(chars) - 1 or chars[i] != chars[i + 1]:
                if pcount > 1:
                    for c in str(pcount):
                        chars.insert(i + 1, c)
                        i += 1
                pcount = 1
                i += 1
            else:
                pcount += 1
                del chars[i + 1]

        return len(chars)
