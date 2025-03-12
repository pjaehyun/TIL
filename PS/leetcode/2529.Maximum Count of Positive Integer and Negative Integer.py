class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        if nums[-1] < 0 or nums[0] > 0: return n

        def bs(x):
            l, r = 0, n-1

            while l < r:
                mid = (l + r) // 2
                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        mid = bs(0)

        return max(mid, n - mid - nums.count(0))