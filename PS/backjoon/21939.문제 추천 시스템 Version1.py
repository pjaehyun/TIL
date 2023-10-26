import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
maxH = []
minH = []
p_dict = defaultdict(int)

for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(maxH, (-l, -p))
    heapq.heappush(minH, (l, p))
    p_dict[p] = l

m = int(input())

for _ in range(m):
    command = list(map(str, input().split()))
    if command[0] == "add":
        p, l = int(command[1]), int(command[2])
        heapq.heappush(maxH, (-l, -p))
        heapq.heappush(minH, (l, p))
        p_dict[p] = l
    elif command[0] == "recommend":
        x = int(command[1])
        if x == 1:
            while p_dict[-maxH[0][1]] != -maxH[0][0]:
                heapq.heappop(maxH)
            print(-maxH[0][1])
        else:
            while p_dict[minH[0][1]] != minH[0][0]:
                heapq.heappop(minH)
            print(minH[0][1])
    else:
        p_dict[int(command[1])] = -1