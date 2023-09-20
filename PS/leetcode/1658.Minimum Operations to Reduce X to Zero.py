class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        l = 0
        max_length = -1
        _sum = 0

        for r in range(len(nums)):
            _sum += nums[r]

            while _sum > target and l <= r:
                _sum -= nums[l]
                l += 1
            
            if _sum == target:
                max_length = max(max_length, r - l + 1)
        return len(nums) - max_length if max_length != -1 else -1