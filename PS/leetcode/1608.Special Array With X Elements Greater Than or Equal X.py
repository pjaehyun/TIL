class Solution:
    def specialArray(self, nums: List[int]) -> int:
        arr = [0] * (max(nums) + 1)
        for num in nums:
            arr[num] += 1
        for i in range(len(arr)):
            if sum(arr[i:]) == i:
                return i
        return -1