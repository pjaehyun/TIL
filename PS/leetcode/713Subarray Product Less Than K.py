class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        l, r, product, count = 0, 0, 1, 0
        n = len(nums)

        while r < n:
            product *= nums[r]
            while product >= k:
                product //= nums[l]
                l += 1
            count += 1 + (r - l)
            r += 1
        return count