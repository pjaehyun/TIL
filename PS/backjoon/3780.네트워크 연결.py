import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find(x):
    if x != UF[x]:
        temp = find(UF[x])
        dist[x] += dist[UF[x]]
        UF[x] = temp
    return UF[x]

def union(x, y):
    UF[x] = y
    dist[x] = abs(x - y) % 1000

T = int(input())

for _ in range(T):
    N = int(input())
    UF = {x:x for x in range(1, N+1)}
    dist = {x:0 for x in range(1, N+1)}

    while True:
        command = list(map(str, input().split()))
        if command[0] == 'O':
            break
        
        if command[0] == 'E':
            find(int(command[1]))
            print(dist[int(command[1])])
        elif command[0] == 'I':
            union(int(command[1]), int(command[2]))