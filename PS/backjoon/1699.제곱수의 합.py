import sys
input = sys.stdin.readline

n = int(input())

dp = [float('inf')] * 100001
dp[0] = 0

squares = []

i = 1
while i*i <= n:
    squares.append(i*i)
    i+=1

for i in range(1, n+1):
    for square in squares:
        if i < square:
            break
        dp[i] = min(dp[i], dp[i-square] + 1)
print(dp[n])