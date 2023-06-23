# 첫번째 풀이
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

# 두번째 풀이
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return 2
        dp = defaultdict(int)
        
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[i] - nums[j]
                dp[(j, diff)] = (dp[(i, diff)] + 1)
        return max(dp.values()) + 1
