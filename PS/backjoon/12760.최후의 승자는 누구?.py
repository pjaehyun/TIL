import sys
input = sys.stdin.readline

n, m = map(int, input().split())

players = []
scores = [0] * n
for _ in range(n):
    players.append(sorted(list(map(int, input().split()))))


for _ in range(m):
    lst = []
    max_value = 0
    for i in range(n):
        temp = players[i].pop()
        max_value = max(max_value, temp)
        lst.append((temp, i))
    
    for score in lst:
        if score[0] == max_value:
            scores[score[1]] += 1

max_score = max(scores)

for i in range(len(scores)):
    if scores[i] == max_score:
        print(i+1, end=" ")