class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans, flips = 0, 0
        for i in range(len(nums)):
            if (nums[i] + flips) % 2 == 0:
                if i > len(nums) - k:
                    return -1
                else:
                    ans += 1
                    flips += 1
                    nums[i] = -1
            if i + 1 >= k:
                flips -= 1 if nums[i - k + 1] < 0 else 0
        return ans