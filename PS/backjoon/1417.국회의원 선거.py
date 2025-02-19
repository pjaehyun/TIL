import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

ds = arr[0]

hq = []

for x in arr[1:]:
    heapq.heappush(hq, -x)

while hq:
    x = heapq.heappop(hq)
    x = -x
    if x < ds:
        break
    ds += 1
    x -= 1
    heapq.heappush(hq, -x)

print(ds - arr[0])