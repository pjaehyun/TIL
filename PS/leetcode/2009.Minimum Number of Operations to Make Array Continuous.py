class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        answer = float('inf')

        for i, num in enumerate(nums):
            e = num + n - 1
            idx = bisect_right(nums, e)

            answer = min(answer, n - (idx - i))
        return answer