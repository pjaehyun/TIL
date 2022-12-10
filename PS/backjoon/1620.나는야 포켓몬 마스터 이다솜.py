import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dogam = {}
for i in range(N):
    poket = input().strip()
    dogam[poket] = i + 1
    dogam[str(i+1)] = poket

for _ in range(M):
    quiz = input().strip()
    print(dogam[quiz])