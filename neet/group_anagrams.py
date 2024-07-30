class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for x in strs:
            if (s := ''.join(sorted(x))) in m:
                m[s].append(x)
            else:
                m[s] = [x]
        return m.values()