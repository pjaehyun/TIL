class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for s, e in tickets:
            graph[s].append(e)
        
        answer = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            answer.append(start)
        dfs("JFK")
        return answer[::-1]