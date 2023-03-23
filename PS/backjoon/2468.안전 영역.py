import sys, copy
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y, height, n):
    for xx, yy in [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]:
        if 0 <= xx < n and 0 <= yy < n and temp[xx][yy] > height:
            temp[xx][yy] = -1
            dfs(xx, yy, height, n)

N = int(input())

sector = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(101):
    temp = copy.deepcopy(sector)
    count = 0
    for j in range(N):
        for k in range(N):
            if temp[j][k] > i:
                count += 1
                dfs(j, k, i, N)
    answer = max(answer, count)
    if count == 0:
        break
print(answer)