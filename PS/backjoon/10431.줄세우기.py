import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    temp = list(map(int, input().split()))
    num, _class = temp[0], temp[1:]
    answer = 0
    for i in range(len(_class)):
        for j in range(i-1, -1, -1):
            if _class[i] < _class[j]:
                answer += 1
    print(num, answer)