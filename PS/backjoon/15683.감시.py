import sys
import copy
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

nesw = [(-1,0), (0,1), (1,0), (0,-1)]

dirs = {
    1:[[0], [1], [2], [3]],
    2:[[1, 3], [0, 2]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5:[[0,1,2,3]]
}

cctv = []
for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] < 6:
            cctv.append((i, j, graph[i][j]))

def sight(road, ds, x, y):
    for d in ds:
        nx, ny = x, y
        while True:
            nx += nesw[d][0]
            ny += nesw[d][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or road[nx][ny] == 6: break
            if road[nx][ny] == 0:
                road[nx][ny] = -1

                

answer = float('inf')

def dfs(count, road):
    global answer
    if count == len(cctv):
        blind = 0
        for r in road:
            blind += r.count(0)
        answer = min(answer, blind)
        return

    temp = copy.deepcopy(road)
    x, y, c = cctv[count]

    for ds in dirs[c]:
        sight(temp, ds, x, y)
        dfs(count+1, temp)
        temp = copy.deepcopy(road)
dfs(0, graph)

print(answer)