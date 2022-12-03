# Pypy3로 제출
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
floor = 0

for height in range(257):
    remove, build = 0, 0

    for i in range(N):
        for j in range(M):
            if ground[i][j] >= height:
                # 현재 블록의 높이가 height보다 크면 블록을 제거하여 인벤토리에 넣는다
                remove += ground[i][j] - height
            else:
                # 현재 블록의 높이가 height보다 낮으면 인벤토리에서 블록을 꺼내서 쌓는다
                build += height - ground[i][j]
    
    # 쌓아야할 블록의 수가 인벤토리의 블록의 수보다 작거나 같을 때
    if remove + B >= build:
        if build + (remove * 2) <= answer:
            answer = build + (remove * 2)
            floor = height
print(answer, floor)