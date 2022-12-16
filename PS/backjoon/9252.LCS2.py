# Pypy3로 제출한 코드, Python3는 시간초과가 났음
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

dp = [[""] * (len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + str1[i-1]
        else:
            dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
print(len(dp[-1][-1]))
print(dp[-1][-1])


# Python3로 제출한 코드, 완성된 Dp배열을 역으로 따라가 공통단어를 추출
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])

if dp[-1][-1] > 0:
    common = []
    i, j = len(str1), len(str2)
    while dp[i][j] != 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            common.append(str1[i-1])
            i -= 1
            j -= 1
    print(''.join(common[::-1]))