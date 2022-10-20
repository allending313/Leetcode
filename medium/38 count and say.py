class Solution:
    def countAndSay(self, n: int) -> str:
        """ naive
        if n == 1:
            return "1"
        
        def say(string):
            prev = ''
            temp = []
            res = ""
            for char in string:
                if char != prev:
                    if len(temp) > 0:
                        res += str(len(temp)) + temp[0]
                    temp = []
                prev = char
                temp.append(char)
                print(temp)
            res += str(len(temp)) + temp[0]
            print(res)
            return res
        
        cns = say("1")
        for _ in range(n-2):
            cns = say(cns)
        return cns
        """
        
        # The first char of our result is 1 so initilize the result
        s = '1'
        
        # As we have taken care of case 1 with n == 1 we start from 2
        while n > 1:
            
            i = 0
            # create new string every iteration and assign it to our res
            ns = ''
            while i < len(s):
                # As we already included the first character so count = 1
                count = 1
                # Check if the prev char is same as next and keep count
                while i+1 < len(s) and s[i] == s[i+1]:
                    i += 1
                    count += 1
                # Finally make the new string
                ns += str(count) + s[i]
                i += 1
            # Assign the newly made string for next iteration to s
            s = ns
            n -= 1
        return s
        