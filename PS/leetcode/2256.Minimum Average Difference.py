class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = [0]

        max_sum = sum(nums)
        max_len = len(nums)

        min_diff = inf
        answer = -1

        for i in range(len(nums)):
            prefix.append((nums[i] + prefix[-1]))
            diff = 0
            if max_len - (i+1) == 0:
                diff = prefix[-1] // (i+1)
            else:
                diff = abs((prefix[-1] // (i+1)) - ((max_sum - prefix[-1]) // (max_len - (i+1))))
            if min_diff > diff:
                min_diff = diff
                answer = i
        return answer