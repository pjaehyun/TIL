N = int(input())

lst = sorted([int(input()) for _ in range(N)], reverse=True)

answer = max([lst[i]*(i+1) for i in range(N)])
print(answer)