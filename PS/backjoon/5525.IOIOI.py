import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

answer = 0
temp = 0
i = 0

while i <= len(S) - 3:
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        temp += 1
        i += 1
    else:
        if temp >= N:
            answer += temp - (N - 1)
        temp = 0
    i += 1

if temp >= N:
    answer += temp - (N - 1)
print(answer)