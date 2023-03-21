# 첫번째 풀이
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0

        answer = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                answer += sum(x for x in range(1, count+1))
                count = 0
        answer += sum(x for x in range(1, count+1))
        return answer

# 두번째 풀이(시간복잡도 개선)
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] == 0:
                dp[i] = dp[i-1] + 1
        return sum(dp)

# 세번째 풀이(첫번째 풀이 코드 리팩토링)
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count, answer = 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            answer += count
        return answer