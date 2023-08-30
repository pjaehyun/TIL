class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n - 1]
        ans = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > last:
                t = nums[i] // last
                if nums[i] % last:
                    t += 1
                last = nums[i] // t
                ans += t - 1
            else:
                last = nums[i]
        return ans