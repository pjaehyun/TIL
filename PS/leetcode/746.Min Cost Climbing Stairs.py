# 첫번째 풀이
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost + [0]

        for i in range(2, len(cost)):
            cost[i] = min(cost[i-2] + cost[i], cost[i-1] + cost[i])
        return cost[-1]
    
# 두번째 풀이
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        dp[-1], dp[-2] = cost[-1], cost[-2]
        for i in range(len(dp) - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])