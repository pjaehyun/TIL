import sys, math
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

seq = []
visited = [False] * N

def backtracking():
    if len(seq) == M:
        print(*seq)
        return
    curr = 0
    for i in range(N):
        if not visited[i] and curr != nums[i]:
            seq.append(nums[i])
            visited[i] = True
            curr = nums[i]
            backtracking()
            visited[i] = False
            seq.pop()
backtracking()