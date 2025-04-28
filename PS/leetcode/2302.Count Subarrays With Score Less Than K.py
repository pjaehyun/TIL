class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        score, sum, cnt=0, 0, 0
        n, l=len(nums), 0
        for r, x in enumerate(nums):
            sum+=x
            score=sum*(r-l+1)
            while score>=k:
                sum-=nums[l]
                l+=1
                score=sum*(r-l+1)
            cnt+=(r-l+1)
        return cnt
        