import sys
from itertools import chain
input = sys.stdin.readline

N = int(input())

def ccw(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

points = []
for _ in range(N):
    x, y, c = map(str, input().split())
    points.append([int(x),int(y)])

points.sort()
stack = []

# Convex Hull(Monotone Chain)
for i in chain(range(len(points)), reversed(range(len(points) - 1))):
    while len(stack) >= 2 and ccw(stack[-2], stack[-1], points[i]) < 0:
        stack.pop()
    stack.append(points[i])
stack.pop()

for i in range(1, (len(stack) + 1) // 2):
    if stack[i] != stack[-1]:
        break
    stack.pop()

print(len(stack))
for s in stack:
    print(s[0], s[1])
