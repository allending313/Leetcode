class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        seen = set()
        
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        for i, char in enumerate(pattern):
            if char not in dic:
                if words[i] in seen:
                    return False
                dic[char] = words[i]
                seen.add(words[i])
                continue
            if dic[char] != words[i]:
                return False
        
        return True
            