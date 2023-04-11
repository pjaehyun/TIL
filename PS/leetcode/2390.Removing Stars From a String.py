class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        dq = deque(list(s))

        while dq:
            char = dq.popleft()

            if stack and char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)