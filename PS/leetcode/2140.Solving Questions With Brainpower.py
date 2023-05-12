class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            point, unable = questions[i]
            if i + unable + 1 >= n:
                dp[i] = max(point, dp[i+1])
            else:
                dp[i] = max(dp[i+unable+1] + point, dp[i+1])
        return max(dp)