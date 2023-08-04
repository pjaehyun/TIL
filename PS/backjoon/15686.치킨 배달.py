import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

chicken = []
houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        if graph[i][j] == 1:
            houses.append((i, j))

def bt(idx, comb, limit):
    if len(comb) == limit:
        comb_chicken.append(comb)
        return
    
    for i in range(idx + 1, len(chicken)):
        bt(i, comb + [chicken[i]], limit)
    
comb_chicken = []
for i in range(len(chicken)):
    bt(i, [chicken[i]], m)

answer = float('inf')
for comb in comb_chicken:
    temp = [float('inf')] * len(houses)
    for chic in comb:
        for i in range(len(houses)):
            temp[i] = min(temp[i], abs(houses[i][0] - chic[0]) + abs(houses[i][1] - chic[1]))
    answer = min(answer, sum(temp))
print(answer)