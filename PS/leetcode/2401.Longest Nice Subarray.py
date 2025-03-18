class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        answer = 1
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                if not (temp & nums[j]):
                    temp |= nums[j]
                    answer = max(answer, j - i + 1)
                else: break
        return answer