class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def sod(x):
            n = 10**9
            
            res = 0
            while x > 0:
                v = x//n
                res += v
                x = x%n
                n //= 10
            return res
        
        nums = sorted([(x, sod(x)) for x in nums], key=lambda x:(x[1],x[0]))
        answer = -1
        for i in range(len(nums)-1):
            if nums[i][1] == nums[i+1][1]:
                answer = max(answer, nums[i][0] + nums[i+1][0])
        return answer