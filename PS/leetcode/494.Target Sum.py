class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def compute_sums(nums, start, end):
            sums = [0]
            for i in range(start, end):
                num = nums[i]
                sums += [s + num for s in sums] + [s - num for s in sums]
            return sums

        n = len(nums)
        mid = n // 2
        sums1 = compute_sums(nums, 0, mid)
        sums2 = compute_sums(nums, mid, n)
        count_map = {}
        for sum_val in sums2:
            count_map[sum_val] = count_map.get(sum_val, 0) + 1

        total = 0
        for sum_val in sums1:
            complement = target - sum_val
            total += count_map.get(complement, 0)
        return total