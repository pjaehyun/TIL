class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        connected_count = defaultdict(int)


        for u, v in adjacentPairs:
            graph[u].append(v)
            connected_count[u] += 1

            graph[v].append(u)
            connected_count[v] += 1
        
        dq = deque()
        visited = set()

        for k, v in connected_count.items():
            if v == 1:
                dq.append(k)
                visited.add(k)
                break
        answer = []
        while dq:
            curr = dq.popleft()
            answer.append(curr)
            for neib in graph[curr]:
                if neib not in visited:
                    visited.add(neib)
                    dq.append(neib)
        
        return answer