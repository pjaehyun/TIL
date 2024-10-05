N = int(input())

answer = 0

lst1 = sorted(list(map(int, input().split())))
lst2 = sorted(list(map(int, input().split())), reverse=True)

for i in range(N):
    answer += (lst1[i] * lst2[i])
print(answer)