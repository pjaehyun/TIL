class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        stack.append(s.pop(0))
        while s:
            if not stack:
                stack.append(s.pop(0))
            if not s:
                return False
            if stack[-1] == '(' and s[0] == ')' or stack[-1] == '{' and s[0] == '}' or stack[-1] == '[' and s[0] == ']':
                stack.pop()
                s.pop(0)
            else: 
                stack.append(s.pop(0))
        if stack:
            return False
        return True
