N = int(input())

lst = sorted([list(map(int, input().split())) for x in range(N)], key=lambda x:(x[1], x[0]))

answer = 1

end = lst[0][1]

for i in range(1, N):
    if lst[i][0] >= end:
        answer += 1
        end = lst[i][1]
print(answer)