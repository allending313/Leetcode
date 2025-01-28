class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        res = (str1, str2)[len(str1) > len(str2)]

        while res != "":
            if str1.count(res) != len(str1) / len(res) or str2.count(res) != len(str2) / len(res):
                res = res[:-1]
                continue
    
            return res
        
        return res

        # def gcd(a: int, b: int) -> int:
        #     return b if a == 0 else gcd(b % a, a)
        # d = gcd(len(str1), len(str2))
        # return str1[: d] if str1[: d] * (len(str2) // d) == str2 and str2[: d] * (len(str1) // d) == str1 else ''
