class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        m = c = sum(x in vowels for x in s[:k])

        for i in range(len(s) - k):
            c += s[i + k] in vowels
            c -= s[i] in vowels
            m = max(m, c)
    
        return m
