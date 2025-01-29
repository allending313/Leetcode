class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(reversed(s.split()))
        
        words = s.split()
        x, y = 0, len(words) - 1

        while x < y:
            words[x], words[y] = words[y], words[x]
            x += 1
            y -= 1
        
        return ' '.join(words)
