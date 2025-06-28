class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [x for i, x in sorted(sorted([(i, x) for i, x in enumerate(nums)], key=lambda x:x[1])[len(nums)-k:], key=lambda x:x[0])]