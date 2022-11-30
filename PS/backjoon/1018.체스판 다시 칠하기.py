N, M = map(int, input().split())
chess = [input() for _ in range(N)]

answer = []
for i in range(N - 7):
    for j in range(M - 7):
        count1 = 0
        count2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if chess[x][y] == 'B':
                        count1 += 1
                    else:
                        count2 += 1
                else:
                    if chess[x][y] == 'W':
                        count1 += 1
                    else:
                        count2 += 1
        answer.append(min(count1, count2))
print(min(answer))