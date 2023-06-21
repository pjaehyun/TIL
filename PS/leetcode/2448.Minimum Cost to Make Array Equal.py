class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def get_value(nums, cost, mid):
            res = 0
            for i in range(len(nums)):
                res += abs(mid - nums[i]) * cost[i]
            return res

        arr = sorted([x for x in zip(nums,cost)], key=lambda x:x[1])
        
        l, r = min(nums), max(nums) + 1

        while l < r:
            mid = (l + r) // 2

            left = get_value(nums, cost, mid)
            right = get_value(nums, cost, mid + 1)
            if left < right:
                r = mid
            else:
                l = mid + 1
        
        return get_value(nums, cost, l)

        