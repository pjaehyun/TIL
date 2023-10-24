import sys
input = sys.stdin.readline

n = int(input())
solutions = sorted(map(int, input().split()))

l, r = 0, n - 1
answer = [solutions[l], solutions[r]]
_sum = abs(solutions[l] + solutions[r])

while l < r:
    fusion = solutions[l] + solutions[r]
    if abs(fusion) < _sum:
        _sum = abs(fusion)
        answer = [solutions[l], solutions[r]]
    
    if fusion < 0:
        l += 1
    else:
        r -= 1
print(*answer)