class Solution:
    def maxSum(self, nums):
        s = set(nums)
        result = sum(x for x in s if x > 0)
        if result == 0:
            result = max(s)
        return result