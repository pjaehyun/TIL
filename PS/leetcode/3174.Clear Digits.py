class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i].isdigit():
                if stack: stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)