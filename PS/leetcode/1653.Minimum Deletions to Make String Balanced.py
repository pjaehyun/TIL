class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        answer = 0
        for i in s:
            if stack and i == 'a' and stack[-1] == 'b':
                answer += 1
                stack.pop()
            else:
                stack.append(i)
        return answer