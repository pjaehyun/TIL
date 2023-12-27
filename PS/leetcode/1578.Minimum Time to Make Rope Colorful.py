class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        sum_cost = 0
        curr = colors[0]
        max_time = neededTime[0]

        for i in range(1, len(neededTime)):
            if curr == colors[i]:
                if neededTime[i] > max_time:
                    sum_cost += max_time
                    max_time = neededTime[i]
                else:
                    sum_cost += neededTime[i]
            else:
                curr = colors[i]
                max_time = neededTime[i]

        return sum_cost