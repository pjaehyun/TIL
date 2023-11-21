class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        answer = 0
        nums_diff = defaultdict(int)

        for num in nums:
            k = num - int(str(num)[::-1])
            answer += nums_diff[k]
            nums_diff[k] += 1
        return answer % (10**9 + 7)