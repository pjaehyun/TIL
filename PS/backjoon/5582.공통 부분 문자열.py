# pypy3로 제출
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

n, m = len(str1), len(str2)

dp = [[0] * (m+1) for _ in range(n+1)]
answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)
print(answer)