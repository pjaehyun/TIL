import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr.sort()
answer = 0

for i in range(n - 1):
    l, r = i + 1, n - 1

    while l <= r:
        mid = (l + r) // 2
        temp = 0
        if arr[i] >= 0.9 * arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    answer += r - i

print(answer)
