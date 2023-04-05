class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        arr1 = nums[:-1]
        arr2 = nums[1:]        
        
        def dp(arr):
            n = len(arr)

            if n <= 2:
                return max(arr)

            dp = [0] * (n+1)

            dp[1], dp[2] = arr[0], arr[1]
            for i in range(3, n+1):
                dp[i] = max(dp[i-2] + arr[i-1], dp[i-3] + arr[i-1])
            return max(dp)

        return max(dp(arr1), dp(arr2))