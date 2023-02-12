# 다른 문제 풀이 참고(BFS로 풀다가 해답을 못냄)
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)

        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        
        answer = 0

        def dfs(node, parent):
            nonlocal answer

            total = 1

            for nei in graph[node]:
                if parent != nei:
                    people, car = dfs(nei, node)

                    total += people

                    answer += car
            cars = ceil(total / seats)

            return total, cars
                        
        dfs(0, None)
        return answer