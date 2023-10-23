import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))

bags = sorted([int(input()) for _ in range(k)], reverse=True)
temp = []
answer = 0
while bags:
    bag = bags.pop()

    while jewels and jewels[0][0] <= bag:
        m, v = heapq.heappop(jewels)
        heapq.heappush(temp, -v)
    if temp:
        answer -= heapq.heappop(temp)

print(answer)
    