import sys
input = sys.stdin.readline

N = int(input())
answer = 0

plane = [[0] * (101) for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            plane[x+i][y+j] = 1
for p in plane:
    answer += sum(p)
print(answer)