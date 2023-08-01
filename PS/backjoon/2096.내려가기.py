import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

max_dp = lst[:]
min_dp = lst[:]

for i in range(n-1):
    n1, n2, n3 = map(int, input().split())
    max_dp = [max(max_dp[0], max_dp[1]) + n1, max(max_dp[0], max_dp[1], max_dp[2]) + n2, max(max_dp[1], max_dp[2]) + n3]
    min_dp = [min(min_dp[0], min_dp[1]) + n1, min(min_dp[0], min_dp[1], min_dp[2]) + n2, min(min_dp[1], min_dp[2]) + n3]
print(max(max_dp), min(min_dp))