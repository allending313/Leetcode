class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # tail = word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):]
        # return ''.join([a + b for a, b in zip(word1, word2)]) + tail

        # res = ""
        # for i in range(m := min(len(word1), len(word2))):
        #     res += word1[i] + word2[i]
        # return res + word1[m:] + word2[m:]
        
        m = min(len(word1), len(word2))
        res = ''.join(a + b for a, b in zip(word1, word2))
        return res + word1[m:] + word2[m:]

        