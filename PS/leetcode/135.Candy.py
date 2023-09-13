class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dp = [1] * len(ratings)

        for i in range(1, n):
            if ratings[i-1] < ratings[i] and dp[i-1] >= dp[i]:
                dp[i] = dp[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i] and dp[i+1] >= dp[i]:
                dp[i] = dp[i+1] + 1
        return sum(dp)
