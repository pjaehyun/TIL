class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        answer = 0

        for i in range(len(nums)):
            total += nums[i]
            answer = max(answer, (total + i) // (i + 1))
        return answer