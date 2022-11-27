class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        answer = 0
        
        for i in range(n):
            for j in range(i):
                count = 0
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    count += dp[j][diff]
                answer += count
                dp[i][diff] += count + 1
        return answer