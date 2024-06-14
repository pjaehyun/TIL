class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nt = 0
        mi = 0

        for num in nums:
            nt = max(nt, num)
            mi += nt - num
            nt += 1
        return mi