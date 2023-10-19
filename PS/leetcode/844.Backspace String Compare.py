class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def read_string(s):
            stack = []

            for char in s:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)
        
        s = read_string(s)
        t = read_string(t)

        return s == t