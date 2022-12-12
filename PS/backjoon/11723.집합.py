import sys

input = sys.stdin.readline

N = int(input())
S = set()

for _ in range(N):
    temp = input().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            S = set(x for x in range(1, 21))
        else:
            S = set()
        continue
    
    command, n = temp[0], int(temp[1])
    if command == "add":
        S.add(n)
    elif command == "check":
        if n in S:
            print(1)
        else:
            print(0)
    elif command == "remove":
        S.discard(n)
    elif command == "toggle":
        if n in S:
            S.remove(n)
        else:
            S.add(n)
