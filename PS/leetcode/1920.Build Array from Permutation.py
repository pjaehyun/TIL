class Solution:
    def buildArray(self, nums):
        n = len(nums)
        for i in range(n):
            nums[i] += (nums[nums[i]] % n) * n
        for i in range(n):
            nums[i] //= n
        return nums