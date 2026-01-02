class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return [k for k, v in Counter(nums).items() if v == len(nums)//2][0]
