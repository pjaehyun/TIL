import sys, math
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

seq = []

def backtracking(n):
    if len(seq) == M:
        print(*seq)
        return
    curr = 0
    for i in range(n, N):
        if curr != nums[i]:
            seq.append(nums[i])
            curr = nums[i]
            backtracking(i)
            seq.pop()
backtracking(0)