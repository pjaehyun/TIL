class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def isSorted(nums, n) -> bool:
            for i in range(1,n):
                if nums[i] < nums[i - 1]: return False
            return True
        ans, n = 0, len(nums)
        while not isSorted(nums, n):
            ans += 1
            min_sum, pos = float('inf'), -1
            for i in range(1,n):
                sum = nums[i - 1] + nums[i]
                if sum < min_sum:
                    min_sum = sum
                    pos = i
            nums[pos - 1] = min_sum
            for i in range(pos, n-1): nums[i] = nums[i + 1]
            n -= 1
        return ans