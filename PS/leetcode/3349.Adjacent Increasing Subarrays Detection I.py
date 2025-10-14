class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - (2*k) + 1):
            prev = nums[i]
            inc1 = True
            for j in range(i+1, i+k):
                if prev < nums[j]:
                    prev = nums[j]
                else: inc1 = False
            
            prev = nums[i+k]
            inc2 = True
            for j in range(i+k+1, i+k+k):
                if prev < nums[j]:
                    prev = nums[j]
                else: inc2 = False
            
            if inc1 and inc2: return True
        return False