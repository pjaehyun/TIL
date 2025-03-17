import sys
input = sys.stdin.readline

n = int(input())

t = int(input())

seq = list(map(int, input().split()))

b = list(map(int, input().split()))

answer = []
for num in b:
    idx = (num-1) % len(seq)

    answer.append(seq[idx])

    for _ in range(idx):
        temp = seq.pop(0)
        seq.append(temp)
print(*answer)    