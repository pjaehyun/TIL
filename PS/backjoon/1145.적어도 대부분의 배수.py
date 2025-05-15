import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

max_gcd = 1000001

answer = 0
for gcd in range(1, max_gcd):
    count = 0
    for num in arr:
        if gcd % num == 0:
            count += 1
    if count >= 3:
        answer = gcd
        break
print(answer)