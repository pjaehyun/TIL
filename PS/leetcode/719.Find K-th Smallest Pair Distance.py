class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            
            if self.issmallpairs(nums, k, mid):
                right = mid
            else:
                left = mid + 1
                
        return left
    
    def issmallpairs(self, nums: List[int], k: int, mid: int) -> bool:
        count = 0
        left = 0
        
        for right in range(1, len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
            
        return count >= k