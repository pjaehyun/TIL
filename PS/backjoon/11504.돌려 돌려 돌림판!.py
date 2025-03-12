import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = int(''.join(list(map(str, input().split()))))
    y = int(''.join(list(map(str, input().split()))))
    arr = list(map(int, input().split()))

    answer = 0

    for i in range(0, n):
        temp = str(arr[i])
        for j in range(i+1, i+m):
            temp += str(arr[j%n])
        if x <= int(temp) <= y:
            answer += 1
    print(answer)