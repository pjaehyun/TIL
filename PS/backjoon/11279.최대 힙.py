import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    command = int(input())
    if command == 0 and not arr:
        print(0)
    elif command == 0:
        n = heapq.heappop(arr)
        print(-n)
    else:
        heapq.heappush(arr, -command)
