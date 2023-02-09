import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

S = input().strip()

answer = set()

def dfs(idx):
    if idx == len(S):
        return
    for i in range(idx, len(S)):
        answer.add(S[idx:i+1])
    dfs(idx+1)

dfs(0)
print(len(answer))