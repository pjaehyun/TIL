class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        _min = 100000

        for idx, num in enumerate(nums):
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                _sum = num + nums[left] + nums[right]
                if abs(target - _sum) < abs(target - _min):
                    _min = _sum
                
                if _sum > target:
                    right -= 1
                else:
                    left += 1
        return _min