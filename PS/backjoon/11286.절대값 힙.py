from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []
nums = defaultdict(int)
for _ in range(N):
    n = int(input())
    if n == 0:
        if heap:
            remove = heapq.heappop(heap)
            if nums[-remove] > 0:
                nums[-remove] -= 1
                print(-remove)
            else:
                nums[remove] -= 1
                print(remove)
        else:
            print(0)
    else:
        heapq.heappush(heap, abs(n))
        nums[n] += 1