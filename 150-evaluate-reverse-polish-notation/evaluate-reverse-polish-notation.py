class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for val in tokens:
            if val not in operators:
                stack.append(val)
            else:
                if val == '+':
                    new_val = int(stack[-2]) + int(stack[-1])
                elif val == '-':
                    new_val = int(stack[-2]) - int(stack[-1])
                elif val == '*':
                    new_val = int(stack[-2]) * int(stack[-1])
                else:
                    new_val = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(new_val)
        return int(stack[-1])