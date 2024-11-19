class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        in_arr=set()
        sum, maxSum, l, Len=0, 0, 0, 0 
        for r, x in enumerate(nums):
            sum+=x
            while l<r and (Len>k-1 or x in in_arr):
                in_arr.remove(nums[l])
                sum-=nums[l]
                l+=1
                Len-=1
            in_arr.add(x)
            Len+=1
            if Len==k:
                maxSum=max(maxSum, sum)
        return maxSum