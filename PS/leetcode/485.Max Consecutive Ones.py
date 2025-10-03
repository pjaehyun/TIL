class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0

        cons = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cons += 1
                answer = max(answer, cons)
            else:
                cons = 0
        return answer