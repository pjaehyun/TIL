class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r, _sum = 0, 0, 0
        answer = 1000000

        while r < n:
            _sum += nums[r]
            while _sum >= target:
                answer = min(answer, r - l)
                _sum -= nums[l]
                l += 1
            r += 1
        return 0 if answer == 1000000 else answer + 1