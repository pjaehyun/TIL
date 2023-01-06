class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        answer = 0
        for i in range(len(costs)):
            if coins >= costs[i]:
                answer += 1
                coins -= costs[i]
        return answer