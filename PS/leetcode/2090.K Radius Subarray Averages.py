class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        answer = [-1] * n
        for i in range(k, n - k):
            if i - k <= 0:
                answer[i] = nums[i+k] // (k * 2 + 1)
            else:
                answer[i] = (nums[i+k] - nums[i - k - 1]) // (k * 2 + 1)
        return answer