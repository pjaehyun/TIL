class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row, col = defaultdict(list), defaultdict(list)
        
        visited = set()
        answer = 0

        for x, y in stones:
            row[x].append(y)
            col[y].append(x)

        # 연결된 모든 스톤들을 탐색
        def dfs(x, y):
            if (x,y) not in visited:
                visited.add((x, y))
                
                for nextY in row[x]:
                    dfs(x, nextY)
                
                for nextX in col[y]:
                    dfs(nextX, y)

        for x, y in stones:
            # 방문하지 않은 스톤이 있을 때 answer += 1
            if (x, y) not in visited:
                dfs(x, y)
                answer += 1
        # 전체 스톤의 수 - 외부 for문에서 dfs를 호출한 수
        return len(stones) - answer
        