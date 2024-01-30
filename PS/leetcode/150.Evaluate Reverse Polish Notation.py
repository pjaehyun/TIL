class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def cal(x, y, o):
            if o == "+":
                return x + y
            elif o == "-":
                return x - y
            elif o == "*":
                return x * y
            else:
                return trunc(x / y)
        oper = "+-*/"
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in oper:
                b = stack.pop()
                a = stack.pop()

                new_val = cal(a, b, tokens[i])
                stack.append(new_val)
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]