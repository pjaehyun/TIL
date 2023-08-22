class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        def recursion(n):
            nonlocal answer
            if n <= 26:
                answer += chr(ord('A') + n-1)
                return
            recursion((n-1) // 26)
            if n % 26 == 0:
                recursion(26)
            else: recursion((n) % 26)
        recursion(columnNumber)
        return answer