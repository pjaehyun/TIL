class Solution(object):
    def minimumIndex(self, nums):
        mpp, left = {}, {}
        for i in nums:
            mpp[i] = mpp.get(i, 0) + 1
        
        for i in range(len(nums) - 1):
            left[nums[i]] = left.get(nums[i], 0) + 1
            mpp[nums[i]] -= 1

            if left[nums[i]] * 2 > (i + 1) and mpp[nums[i]] * 2 > (len(nums) - i - 1):
                return i
        return -1