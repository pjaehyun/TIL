class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        i, j = 0, 0
        
        while j < n:
            if j > 0 and nums[j] - nums[j - 1] != 1:
                i = j
            while i < j and j - i + 1 > k:
                i += 1
            if j - i + 1 == k:
                ans[j - k + 1] = nums[j]
            j += 1
        
        return ans