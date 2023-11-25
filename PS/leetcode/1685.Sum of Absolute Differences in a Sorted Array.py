class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.append(0)
        A = 0
        B = sum(nums[1:])
        answer = [0] * n
        for i in range(n):
            answer[i] = (2*i-n+1) * nums[i] + B - A
            A += nums[i]
            B -= nums[i+1]
        return answer