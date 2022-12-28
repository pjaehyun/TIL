import sys
input = sys.stdin.readline

N = int(input())
video = [list(input().strip()) for _ in range(N)]
answer = ""
def recursion(x, y, n):
    global answer
    first = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[i][j] != first:
                answer += "("
                # 재귀 호출
                for k in range(2):
                    for z in range(2):
                        recursion(x + (n // 2 * k), y + (n // 2 * z), n // 2)
                answer += ")"
                return
                
    answer += first
recursion(0, 0, N)
print(answer)
