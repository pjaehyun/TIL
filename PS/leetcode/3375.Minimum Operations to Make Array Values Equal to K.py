class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums), reverse=True)
        if nums[-1] < k: return -1
        answer = 0
        for i in range(1, len(nums)):
            if nums[i] < k:
                return -1
            answer += 1
        return answer+1 if nums[-1] != k else answer
