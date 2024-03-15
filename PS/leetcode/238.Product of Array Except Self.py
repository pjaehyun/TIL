class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n+1)
        prefix[1] = nums[0]

        suffix = [1] * (n+1)
        suffix[-2] = nums[-1]

        for i in range(2, n+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        answer = [0] * n
        for i in range(n):
            answer[i] = prefix[i] * suffix[i+1]
        return answer
