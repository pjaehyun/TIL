import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

sticker = [0] * (n+1)

answer = 0
temp = 0
for i in range(len(arr)):
    if sticker[arr[i]] >= 1:
        sticker[arr[i]] = 0
        temp -= 1
    else:
        sticker[arr[i]] += 1
        temp += 1
    answer = max(answer, temp)

print(answer)