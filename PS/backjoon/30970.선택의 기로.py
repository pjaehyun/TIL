import sys
input = sys.stdin.readline

n = int(input())

max_arr = []
min_arr = []

for _ in range(n):
    q, p = map(int, input().split())
    max_arr.append((q, p))
    min_arr.append((q, p))

max_arr.sort(key=lambda x: (x[0], -x[1]), reverse=True)
min_arr.sort(key=lambda x: (x[1], -x[0]))

print(max_arr[0][0], max_arr[0][1], max_arr[1][0], max_arr[1][1])
print(min_arr[0][0], min_arr[0][1], min_arr[1][0], min_arr[1][1])