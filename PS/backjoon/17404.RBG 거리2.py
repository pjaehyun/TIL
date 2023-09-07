import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

houses = [list(map(int, input().split())) for _ in range(n)]

R = [[float('inf')] * 3 for _ in range(n)]
R[0][0] = houses[0][0]

G = [[float('inf')] * 3 for _ in range(n)]
G[0][1] = houses[0][1]

B = [[float('inf')] * 3 for _ in range(n)]
B[0][2] = houses[0][2]

for i in range(1, n):
    R[i][0] = min(R[i][0], R[i-1][1] + houses[i][0], R[i-1][2] + houses[i][0])
    R[i][1] = min(R[i][1], R[i-1][0] + houses[i][1], R[i-1][2] + houses[i][1])
    R[i][2] = min(R[i][2], R[i-1][0] + houses[i][2], R[i-1][1] + houses[i][2])

    G[i][0] = min(G[i][0], G[i-1][1] + houses[i][0], G[i-1][2] + houses[i][0])
    G[i][1] = min(G[i][1], G[i-1][0] + houses[i][1], G[i-1][2] + houses[i][1])
    G[i][2] = min(G[i][2], G[i-1][0] + houses[i][2], G[i-1][1] + houses[i][2])

    B[i][0] = min(B[i][0], B[i-1][1] + houses[i][0], B[i-1][2] + houses[i][0])
    B[i][1] = min(B[i][1], B[i-1][0] + houses[i][1], B[i-1][2] + houses[i][1])
    B[i][2] = min(B[i][2], B[i-1][0] + houses[i][2], B[i-1][1] + houses[i][2])

print(min(R[-1][1], R[-1][2], G[-1][0], G[-1][2], B[-1][1], B[-1][0]))