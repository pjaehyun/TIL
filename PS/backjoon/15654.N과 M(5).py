import sys, math
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

answer = []

visited = set()
def backtracking(seq, nums):
    if len(seq) == M:
        answer.append(seq[:])
    
    for n in nums:
        if n not in visited:
            visited.add(n)
            seq.append(n)
            backtracking(seq, nums)
            visited.remove(n)
            seq.pop()

for n in nums:
    if n not in visited:
        visited.add(n)
        backtracking([n], nums)
        visited.remove(n)
answer.sort()

for i in range(len(answer)):
    for j in range(len(answer[i])):
        print(answer[i][j], end=" ")
    print()