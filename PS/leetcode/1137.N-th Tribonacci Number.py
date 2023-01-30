# 첫번째 풀이(재귀로 풀게되면 시간초과)
class Solution:
    def tribonacci(self, n: int) -> int:
        def tribonacci(n):
            if n == 0:
                return 0

            if n == 2 or n == 1:
                return 1
            
            return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        return tribonacci(n)

# 두번째 풀이
class Solution:
    def tribonacci(self, n: int) -> int:

        dp = [0 for _ in range(38)]

        dp[0], dp[1], dp[2] = 0, 1, 1
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
