import sys
input = sys.stdin.readline

s = input().strip()
arr = [[0] * 26]
arr[0][ord(s[0])-97] = 1
for i in range(1, len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97] += 1

for _ in range(int(input())):
    a, l, r = map(str, input().strip().split())
    l, r = int(l), int(r)
    if l == 0:
        print(arr[r][ord(a)-97])
    else:
        print(arr[r][ord(a)-97]-arr[l-1][ord(a)-97])
