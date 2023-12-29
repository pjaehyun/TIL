class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        if n == d:
            return sum(jobDifficulty)

        dp = [int(1e9)] * n
        dp[0] = jobDifficulty[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], jobDifficulty[i])

        dpPrev = dp.copy()

        for i in range(1, d):
            dp = [int(1e9)] * n
            for j in range(i, n):
                lastDayDifficulty = jobDifficulty[j]
                tmpMin = lastDayDifficulty + dpPrev[j - 1]

                for t in range(j - 1, i - 1, -1):
                    lastDayDifficulty = max(lastDayDifficulty, jobDifficulty[t])
                    tmpMin = min(tmpMin, lastDayDifficulty + dpPrev[t - 1])

                dp[j] = tmpMin
            dpPrev = dp.copy()

        return dp[n - 1]
        