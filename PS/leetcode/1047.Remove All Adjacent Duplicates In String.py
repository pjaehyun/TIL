
# while
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        dq = deque(list(s))

        while dq:
            char = dq.popleft()
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

# for
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)