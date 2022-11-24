from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
comp = sorted(set(arr))
count = defaultdict(int)

for i in range(len(comp)):
    count[comp[i]] = i

for a in arr:
    print(count[a], end=" ")
