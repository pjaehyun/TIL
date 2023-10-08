import sys
input = sys.stdin.readline

n = int(input())
coor = [list(map(int, input().split())) for _ in range(n)]

coor.append(coor[0])

x_sum = 0
y_sum = 0

for i in range(len(coor) - 1):
    x_sum += (coor[i][0] * coor[i+1][1])
    y_sum += (coor[i][1] * coor[i+1][0])
answer = round((x_sum - y_sum) / 2, 1)

if answer < 0:
    answer *= -1
print(answer)