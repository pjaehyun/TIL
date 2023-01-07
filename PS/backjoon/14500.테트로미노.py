import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

answer = 0
def dfs(x, y, _sum, block):
    global answer
    if _sum + _max*(4-block) <= answer:
        return
        
    if block == 4:
        answer = max(answer, _sum)
        return
    for xx, yy in [[x,y+1], [x+1,y], [x,y-1], [x-1,y]]:
        if 0 <= xx < N and 0 <= yy < M and not visited[xx][yy]:
            if block == 2:
                # ㅏ, ㅓ, ㅗ, ㅜ 탐색
                visited[xx][yy] = True
                dfs(x, y, _sum + arr[xx][yy], block+1)
                visited[xx][yy] = False

            visited[xx][yy] = True
            dfs(xx, yy, _sum + arr[xx][yy], block+1)
            visited[xx][yy] = False

_max = max(map(max, arr))
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,arr[i][j],1)
        visited[i][j] = False
print(answer)