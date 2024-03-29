class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, count = 0, 0
        high = max(nums)        
        n = len(nums)
        answer = 0
        
        for r in range(n):
            if nums[r] == high:
                count += 1
            
            while count >= k:
                answer += n - r
                if nums[l] == high:
                    count -= 1
                l += 1
        return answer