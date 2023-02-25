class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        answer = 0

        for i in range(1, len(prices)):
            answer = max(answer, prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]

        return answer