# 풀이 실패로 해답참고, 그러나 해답을 봐도 이해가 안감
# https://www.acmicpc.net/problem/1126 해당 문제로 다시 도전해야하는 문제임
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        _sum = sum(rods)
        dp = [-1] * (_sum + 1)
        dp[0] = 0

        for rod in rods:
            dp_copy = dp[:]

            for i in range(_sum - rod + 1):
                if dp_copy[i] < 0:
                    continue
                dp[i + rod] = max(dp[i+rod], dp_copy[i])
                dp[abs(i-rod)] = max(dp[abs(i-rod)], dp_copy[i] + min(i, rod))
        return dp[0]