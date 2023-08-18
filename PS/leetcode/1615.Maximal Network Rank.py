class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = [0 for _ in range(n)]
        graph = defaultdict(list)
        for road in roads:
            graph[road[0]].append(road[1])
            count[road[0]] += 1

            graph[road[1]].append(road[0])
            count[road[1]] += 1
        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                if j in graph[i]:
                    answer = max(answer, count[i] + count[j] - 1)
                else:
                    answer = max(answer, count[i] + count[j])
        return answer