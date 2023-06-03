class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # make graph
        graph = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        
        dq = deque()
        dq.append((headID, 0))
        answer = 0
        while dq:
            node, time = dq.popleft()
            for neib in graph[node]:
                dq.append((neib, time + informTime[node]))
            answer = max(answer, time)
        return answer