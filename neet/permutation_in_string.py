class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = Counter(s1)
        for i, c in enumerate(s2):
            if c not in p:
                continue
            if p == Counter(s2[i:i+len(s1)]):
                return True
        return False