class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [defaultdict(int) for i in range(n)]
        
        answer = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j][diff] + 1
                answer = max(answer, dp[i][diff])
        return answer + 1
