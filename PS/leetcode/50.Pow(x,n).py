class Solution:
    def myPow(self, x: float, n: int) -> float:

        def dfs(x, n):
            if x == 0: return 0
            if n == 0: return 1

            v = dfs(x, n//2)
            v = v * v
            if n % 2 != 0:
                return v * x
            else:
                return v
        
        answer = dfs(x, abs(n))
        if n < 0:
            return 1/answer
        return answer