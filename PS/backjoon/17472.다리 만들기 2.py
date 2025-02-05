import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(1, n+1)}
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False
        
        if rx < ry:
            self.uf[ry] = rx
        else:
            self.uf[rx] = ry
        return True
    
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]
    

def dfs(x, y):
    for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1 and not visited[nx][ny]:
            arr[nx][ny] = num
            visited[nx][ny] = True
            dfs(nx, ny)

def bridge(island, x, y):
    for nx in range(x+1, n):
        if arr[nx][y] == island: break

        if arr[nx][y] != 0:
            if nx-x-1 > 1:
                mst.append((island, arr[nx][y], nx-x-1))
            break
    
    for nx in range(x-1, -1, -1):
        if arr[nx][y] == island: break

        if arr[nx][y] != 0:
            if x-nx-1 > 1:
                mst.append((island, arr[nx][y], x-nx-1))
            break

    for ny in range(y+1, m):
        if arr[x][ny] == island: break

        if arr[x][ny] != 0:
            if ny-y-1 > 1:
                mst.append((island, arr[x][ny], ny-y-1))
            break

    for ny in range(y-1, -1, -1):
        if arr[x][ny] == island: break

        if arr[x][ny] != 0:
            if y-ny-1 > 1:
                mst.append((island, arr[x][ny], y-ny-1))
            break


num = 1
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            arr[i][j] = num
            visited[i][j] = True
            dfs(i, j)
            num += 1
num = num - 1
 
mst = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            bridge(arr[i][j], i, j)
mst.sort(key=lambda x:x[2])
answer = 0
uf = UnionFind(num)
edge_count = 0
for x, y, w in mst:
    if uf.union(x, y):
        answer += w
        edge_count += 1
if answer == 0 or edge_count != num-1:
    answer = -1
print(answer)