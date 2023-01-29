import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [x+1 for x in range(N)]

def backtracking(num, part, count):
    if count == M:
        for p in part:
            print(p, end=" ")
        print()
        return
    for n in arr[num-1:]:
        part.append(n)
        backtracking(part[-1], part[:], count+1)
        part.pop()

backtracking(1, [], 0)

