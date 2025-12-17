class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        first_price = prices[0]
        dp = [[0, -first_price, first_price] for _ in range(k + 1)]
        n = len(prices)
        
        for day in range(1, n):
            curr_price = prices[day]
            for trans in range(k, 0, -1):
                prev_profit = dp[trans - 1][0]
                dp[trans][0] = max(dp[trans][0], dp[trans][1] + curr_price, dp[trans][2] - curr_price)
                dp[trans][1] = max(dp[trans][1], prev_profit - curr_price)
                dp[trans][2] = max(dp[trans][2], prev_profit + curr_price)
        
        return dp[k][0]