import sys
input = sys.stdin.readline

n = int(input())

arr = [input().strip() for _ in range(n)]

name_len = len(arr[0])

answer = ""
for i in range(name_len):
    word = arr[0][i]
    for j in range(1, n):
        if arr[j][i] != word:
            word = "?"
            break
    answer += word
print(answer)