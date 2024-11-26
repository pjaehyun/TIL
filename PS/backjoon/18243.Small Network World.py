import sys
input = sys.stdin.readline

def find(arr):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: continue
            if network[i][j] > 6:
                return "Big World!"
    return "Small World!"

n, k = map(int, input().split())
network = [[100000] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())

    network[a][b] = 1
    network[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if network[i][j] > network[i][k] + network[k][j]:
                network[i][j] = network[i][k] + network[k][j]

print(find(network))
