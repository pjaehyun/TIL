class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n, k2=len(prices), k//2
        Sum=list(accumulate((strategy[i]*prices[i] for i in range(n)),initial=0))
        modify=sum(prices[k2:k])
        profit=max(Sum[n], modify+Sum[n]-Sum[k])

        for i in range(1, n+1-k):
            modify+=prices[i+k-1]-prices[i+k2-1]
            profit=max(profit, modify+Sum[n]-Sum[i+k]+Sum[i])
        return profit
        