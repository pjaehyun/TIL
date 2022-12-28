import sys
input = sys.stdin.readline

N = int(input())
dp = [4 for _ in range(N+1)]
dp[0], dp[1] = 0, 1

for i in range(2, N+1):
    _min = float('inf')
    j = 1

    while j**2 <= i:
        _min = min(_min, dp[i-j**2])
        j += 1
    dp[i] = _min + 1
print(dp[N])