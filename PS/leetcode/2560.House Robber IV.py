class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 1, 10**9
        while l < r:
            m, t, i = (l + r) // 2, 0, 0
            while i < len(nums) and t < k:
                if nums[i] <= m:
                    t += 1
                    i += 2
                else:
                    i += 1
            l, r = (m + 1, r) if t < k else (l, m)
        return l