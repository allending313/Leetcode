class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        x, y = 0, len(s) - 1
        l = list(s)

        while x < y:
            while x < y and l[x] not in vowels:
                x += 1
            while x < y and l[y] not in vowels:
                y -= 1
            l[x], l[y] = l[y], l[x]
            x += 1
            y -= 1
        
        return ''.join(l)