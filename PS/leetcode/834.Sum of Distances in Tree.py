# 처음에 워셜 플로이드로 모든 노드의 거리를 구하는 방식으로 풀었지만 시간복잡도에서 통과하지못하여 풀이 변경(다른 사람 풀이 참고)
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        count = [1] * n
        answer = [0] * n
        for s,e in edges:
            graph[s].add(e)
            graph[e].add(s)
        
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    answer[node] += (answer[child] + count[child])
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    dfs2(child, node)
            
        dfs(0,None)
        dfs2(0,None)
        return answer