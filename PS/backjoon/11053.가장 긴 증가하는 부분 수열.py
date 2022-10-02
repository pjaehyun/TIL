# 완전 탐색
N = int(input())
lst = list(map(int, input().split()))
dp = [1 for _ in range(1001)]

for i in range(len(lst)):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))


# 이분탐색
N = int(input())
lst = list(map(int, input().split()))
answer = []

def binary_search(start, end, num):
    while start < end:
        mid = (start + end) // 2
        if answer[mid] < num:
            start = mid + 1
        else:
            end = mid 
    return start

answer.append(lst.pop(0))

while lst:
    num = lst.pop(0)
    if num > answer[-1]:
        answer.append(num)
    else:
        idx = binary_search(0, len(answer) - 1, num)
        answer[idx] = num
print(len(answer))



