n = int(input())

towers = list(map(int, input().split()))

stack = []
answer = ['0'] * n

for i in range(len(towers) - 1, -1, -1):
    while stack and stack[-1][0] <= towers[i]:
        value, idx = stack.pop()
        answer[idx] = str(i+1)
    else:
        stack.append((towers[i], i))

print(' '.join(answer))