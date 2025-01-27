class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * numCourses
        seq = [0] * numCourses
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)
            seq[y] |= 1 << x
            indegree[y] += 1
        
        dq = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)
        
        while dq:
            curr = dq.popleft()

            for neib in graph[curr]:
                seq[neib] |= seq[curr]
                indegree[neib] -= 1
                if indegree[neib] == 0:
                    dq.append(neib)
        
        answer = []

        for query in queries:
            answer.append((seq[query[1]] & (1 << query[0])) != 0)
        return answer