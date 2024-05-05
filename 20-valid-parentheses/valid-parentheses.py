class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            elif item == ')' and stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif item == ']' and stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif item == '}' and stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        if not stack:
            return True
        return False