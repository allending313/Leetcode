class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            if (key := "".join(sorted(list(word)))) in dic:
                if dic[key]:
                    dic[key].append(word)
            else:
                dic[key] = [word]
        return [x for x in dic.values()]