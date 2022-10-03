N = int(input())

graph = [list(input()) for _ in range(N)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
comp = 0
house_count = []

# 단지 내 집의 수 카운트 
def dfs(x, y):
    graph[x][y] = '0'
    ret = 1
    for i in range(4):
        xx, yy = dx[i] + x, dy[i] + y
        if xx < 0 or xx >= N or yy < 0 or yy >= len(graph[0]) or graph[xx][yy] == '0':
            continue
        ret += dfs(xx, yy)
    return ret

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == '1':
            comp += 1
            ret = dfs(i,j)
            house_count.append(ret)
print(comp)
for h in sorted(house_count):
    print(h)