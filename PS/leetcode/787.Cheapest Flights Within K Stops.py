class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        
        min_cost = [inf for _ in range(n)]

        dq = deque()
        dq.append((src, 0))
        step = 0
        while dq and step <= k:
            # 새로 추가되는 요소는 다음스텝에 진행하기 위해 dq의 길이만큼 반복문을 돌리면서 pop을 진행
            for _ in range(len(dq)):
                start, price = dq.popleft()
                for nei, cost in graph[start]:
                    if price + cost > min_cost[nei]:
                        continue
                    min_cost[nei] = price+cost
                    dq.append((nei, min_cost[nei]))
            step += 1
        return min_cost[dst] if min_cost[dst] != inf else -1
