class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        sell = 0

        for i in range(1, len(prices)):
            # 팔았을 떄 buy = prices[i]가 되어야 한다.
            if sell < prices[i] - buy + sell:
                sell = prices[i] - buy + sell
                buy = prices[i]
                
            if prices[i] < buy:
                buy = prices[i]
        return sell
