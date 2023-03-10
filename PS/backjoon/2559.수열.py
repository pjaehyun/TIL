import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))

prefix_sum = [0] * (N+1)
continuous_sum = [0] * (N+1)

for i in range(1, N+1):
    if i >= K:
        continuous_sum[i] = prefix_sum[i-1] + arr[i-1] - prefix_sum[i-K]
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]    
print(max(continuous_sum[K:]))
