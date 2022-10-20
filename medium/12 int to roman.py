class Solution:
    def intToRoman(self, num: int) -> str:
        """ naive
        digits = [int(x) for x in str(num)]
        while len(digits) < 4:
            digits.insert(0, 0)
        res = ""
        
        for i in range(4):
            if i == 0:
                for _ in range(digits[i]): res += 'M'
            elif i == 1:
                if digits[i] < 4:
                    for _ in range(digits[i]): res += 'C'
                elif digits[i] == 4:
                    res += "CD"
                elif digits[i] == 9:
                    res += "CM"
                else:
                    res += "D"
                    for _ in range(digits[i]-5): res += 'C'
            elif i == 2:
                if digits[i] < 4:
                    for _ in range(digits[i]): res += 'X'
                elif digits[i] == 4:
                    res += "XL"
                elif digits[i] == 9:
                    res += "XC"
                else:
                    res += "L"
                    for _ in range(digits[i]-5): res += 'X'
            elif i == 3:
                if digits[i] < 4:
                    for _ in range(digits[i]): res += 'I'
                elif digits[i] == 4:
                    res += "IV"
                elif digits[i] == 9:
                    res += "IX"
                else:
                    res += "V"
                    for _ in range(digits[i]-5): res += 'I'
        return res
        """
        dic = {"M": 1000, "CM": 900, "D": 500, "CD": 400,
	   "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,
	   "IX": 9, "V": 5, "IV": 4, "I": 1}

        output = ""
        for key, value in dic.items():
            output += key * (num // value)
            if num // value != 0:
                num -= (value * (num // value))

        return output
            
