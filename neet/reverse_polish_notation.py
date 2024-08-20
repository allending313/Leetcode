class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "/": lambda a, b: int(b / a),
            "*": lambda a, b: a * b
        }
        for i in tokens:
            if i in ops:
                stack.append(ops[i](stack.pop(), stack.pop()))
            else:
                stack.append(int(i))
        return stack[0]
       
        # i = 0
        # while i < len(tokens):
        #     match tokens[i]:
        #         case '+':
        #             tokens[i] = int(tokens[i - 2]) + int(tokens[i - 1])
        #             tokens = tokens[:i - 2] + tokens[i:]
        #             i -= 1
        #         case '-':
        #             tokens[i] = int(tokens[i - 2]) - int(tokens[i - 1])
        #             tokens = tokens[:i - 2] + tokens[i:]
        #             i -= 1
        #         case '*':
        #             tokens[i] = int(tokens[i - 2]) * int(tokens[i - 1])
        #             tokens = tokens[:i - 2] + tokens[i:]
        #             i -= 1
        #         case '/':
        #             tokens[i] = int(tokens[i - 2]) / int(tokens[i - 1])
        #             tokens = tokens[:i - 2] + tokens[i:]
        #             i -= 1
        #         case _:
        #             i += 1

        # return int(tokens[0])