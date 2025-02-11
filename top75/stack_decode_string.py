class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        chars = []
        prev = ''

        for x in s:
            if x.isdigit():
                if prev.isdigit():
                    nums.append(nums.pop() + x)
                else:
                    nums.append(x)
            elif x.isalpha():
                if prev.isalpha():
                    chars.append(chars.pop() + x)
                else:
                    chars.append(x)
            elif x == '[':
                chars.append('[')
            elif x == ']':
                n = nums.pop()
                c = ''
                y = chars.pop()
                while y != '[':
                    c = y + c
                    y = chars.pop()
                chars.append(int(n) * c)
            prev = x
        
        return ''.join(chars)

        # stack = []
        # for x in s:
        #     if x != ']':
        #         stack.append(x)
        #     else:
        #         c = ''
        #         while stack[-1] != '[':
        #             c = stack.pop() + c
        #         stack.pop()

        #         n = ''
        #         while stack and stack[-1].isdigit():
        #             n = stack.pop() + n
                
        #         stack.append(int(n) * c)
            
        # return ''.join(stack)