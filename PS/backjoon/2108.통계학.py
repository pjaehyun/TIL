from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

arr = []
count = defaultdict(int)

for i in range(N):
    n = int(input())
    arr.append(n)
    count[n] += 1
arr.sort()

max_value = max(count.values())

modes = []
for k, v in count.items():
    if v == max_value:
        modes.append(k)

modes.sort()

print(int(round(sum(arr)/len(arr), 0)))
print(arr[len(arr) // 2])
print(modes[0] if len(modes) == 1 else modes[1])
print(abs(arr[0] - arr[-1]))