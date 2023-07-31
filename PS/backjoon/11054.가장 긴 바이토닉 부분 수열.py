import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
r_lst = lst[::-1]
increase = [1] * n
decrease = [1] * n
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            increase[i] = max(increase[i], increase[j] + 1)        
        if r_lst[i] > r_lst[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
answer = 0
for i in range(n):
    answer = max(answer, increase[i] + decrease[n-i-1] - 1)
print(answer)