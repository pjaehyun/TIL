class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        answer = max(nums)
        for i in range(n):
            total = nums[i]
            pre = nums[i]
            for j in range(i+1, n):
                if pre < nums[j]:
                    pre = nums[j]
                    total += nums[j]
                else:
                    break
            answer = max(answer, total)
        return answer