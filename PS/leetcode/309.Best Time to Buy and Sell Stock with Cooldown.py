class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0
            
        dp = [0] * (n+1)
        
        min_price = prices[0]
        for i in range(1, n+1):
            min_price = min(min_price, prices[i-1]-dp[i-2])
            dp[i] = max(dp[i-1], prices[i-1]-min_price)
        return dp[-1]
        