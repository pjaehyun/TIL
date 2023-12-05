class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0
        while n != 1:
            answer += (n//2)
            if n % 2 == 0:
                n = n // 2
            else:
                n = n // 2 + 1
        return answer