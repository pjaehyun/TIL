class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    answer = max(answer, (nums[i] - nums[j]) * nums[k])
        return answer