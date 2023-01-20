import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N, L = map(int, input().split())

drawer = {x:x for x in range(1, L+1)}
have = {x:False for x in range(1, L+1)}

def find(x):
    if x != drawer[x]:
        drawer[x] = find(drawer[x])
    return drawer[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    drawer[rootX] = rootY



for i in range(N):
    x, y = map(int, input().split())

    if not have[x]:
        have[x] = True
        union(x, y)
        print("LADICA")
    elif not have[y]:
        have[y] = True
        union(y, x)
        print("LADICA")
    elif not have[find(x)]:
        have[find(x)] = True
        union(x, y)
        print("LADICA")
    elif not have[find(y)]:
        have[find(y)] = True
        union(y, x)
        print("LADICA")
    else:
        print("SMECE")
