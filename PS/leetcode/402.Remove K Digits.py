class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []

        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        stack = stack[:-k] if k > 0 else stack
        answer = ''.join(stack).lstrip('0')

        return answer if answer else '0'