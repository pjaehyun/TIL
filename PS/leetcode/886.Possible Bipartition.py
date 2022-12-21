# Dfs 풀이 방식
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        partition = [0] * (n+1)

        for n1, n2 in dislikes:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        if len(graph) == 0:
            return True

        def dfs(n, group):
            if partition[n] == 0:
                partition[n] = group
            elif partition[n] == -group:
                return False
            else:
                return True
            
            con = True
            for dis in graph[n]:
                con = con and dfs(dis, -group)
            return con
            
        con = True
        for i in range(1, n+1):
            if partition[i] == 0:
                con = con and dfs(i, 1)
                if not con: return False
        return True


# Bfs 풀이 방식
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        partition = [0] * (n+1)

        for n1, n2 in dislikes:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def bfs(n):
            dq = deque()
            dq.append(n)
            partition[n] = 1

            while dq:
                cur = dq.popleft()
                cur_group = partition[cur]
                
                for dis in graph[cur]:
                    if partition[dis] == cur_group:
                        return False
                    elif partition[dis] == -cur_group:
                        continue
                    partition[dis] = -cur_group
                    dq.append(dis)
            return True

        for i in range(1, n+1):
            if partition[i] == 0:
                if not bfs(i):
                    return False
        return True