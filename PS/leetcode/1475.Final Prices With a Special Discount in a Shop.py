class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = [x for x in prices]

        for i in range(n):
            for j in range(i+1, n):
                if answer[i] >= prices[j]:
                    answer[i] = answer[i] - prices[j]
                    break
        return answer