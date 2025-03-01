import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

rooms = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    for i in range(x, y):
        rooms[i] = 1

print(rooms.count(0) - 1)