class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * (n+1)

        graph = defaultdict(list)
        for i in range(len(relations)):
            graph[relations[i][0]].append(relations[i][1])
            indegree[relations[i][1]] += 1
        
        dq = deque()

        for i in range(1, n+1):
            if indegree[i] == 0:
                dq.append(i)
        
        answer = [0] + time[:]

        while dq:
            for _ in range(len(dq)):
                curr = dq.popleft()
                for neib in graph[curr]:
                    answer[neib] = max(answer[neib], time[neib-1] + answer[curr])
                    indegree[neib] -= 1
                    if indegree[neib] == 0:
                        dq.append(neib)
        return max(answer)
