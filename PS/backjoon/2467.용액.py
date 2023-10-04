import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))

i, j = 0, n-1
answer = [solutions[i], solutions[j]]

while i < j:
    mix = solutions[i] + solutions[j]
    if abs(mix) <= abs(answer[0] + answer[1]):
        answer[0] = solutions[i]
        answer[1] = solutions[j]
    if mix < 0:
        i += 1
    elif mix > 0:
        j -= 1
    else:
        break
print(answer[0], answer[1])