class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        answer = 0
        
        for i in range(len(nums) - 1):
            _min = lower - nums[i]
            _max = upper - nums[i]

            start = bisect_left(nums, _min, i+1)
            end = bisect_right(nums, _max, i+1)

            answer += (end - start)
        return answer