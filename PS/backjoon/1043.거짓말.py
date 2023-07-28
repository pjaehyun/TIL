import sys

input = sys.stdin.readline

n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]

UF = {x:x for x in range(1, n+1)}

def find(x):
    if UF[x] != x:
        UF[x] = find(UF[x])
    return UF[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX in truth:
        UF[rootY] = rootX
    elif rootY in truth:
        UF[rootX] = rootY
    else:
        if rootX < rootY:
            UF[rootY] = rootX
        else:
            UF[rootX] = rootY

answer = 0
parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(party)
    for i in range(len(party) - 1):
        union(party[i], party[i+1])

for party in parties:
    check = True
    for i in range(len(party)):
        if find(party[i]) in truth:
            check = False
            break
    if check:
        answer += 1
print(answer)