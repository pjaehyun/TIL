import sys
input = sys.stdin.readline

def ccw(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])

points.sort()
start = points[0]
points.remove(start)

# 반 시계 방향으로 정렬
inf = []
for i in range (n-1):
    if start[0] == points[i][0]:
        inf.append(points[i])
    else:
        points[i].append((start[1]-points[i][1])/(start[0]-points[i][0]))
for i in inf:
    points.remove(i)
points.sort(key=lambda x : x[2])
for i in inf:
    points.append(i)

stack = []

stack.append(start)
stack.append(points[0])

# Convex Hull(Graham's Scan)
for i in range(1, len(points)):
    while len(stack) >= 2 and ccw(stack[-2], stack[-1], points[i]) <= 0:
        stack.pop()
    stack.append(points[i])

print(len(stack))