# 첫번째 풀이(다익스트라 알고리즘에서 우선순위 큐를 쓰는 이유가 없어짐)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        def dijkstra(start):
            distances = [0 for _ in range(n)]
            distances[start] = 1
            hq = []
            heapq.heappush(hq, start)
            while hq:
                curr = heapq.heappop(hq)
                for neib, weight in graph[curr]:
                    if distances[neib] < distances[curr] * weight:
                        distances[neib] = distances[curr] * weight
                        heapq.heappush(hq, neib)
            return distances[end]
        return dijkstra(start)

# 두번째 풀이(코드 개선 및 시간복잡도 개선)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))


        distances = [0 for _ in range(n)]
        distances[start] = 1
        hq = []
        heapq.heappush(hq, (-1, start))
        while hq:
            dist, curr = heapq.heappop(hq)

            if curr == end: return -dist
            if distances[curr] > -dist:
                continue

            for neib, weight in graph[curr]:
                cost = weight * dist
                if distances[neib] < -cost:
                    distances[neib] = -cost
                    heapq.heappush(hq, (cost, neib))

        return distances[end]