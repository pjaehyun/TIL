import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

l, r = 0, n - 1
answer = 0

while l != r:
    if nums[l] + nums[r] == x:
        answer += 1
        l += 1
    elif nums[l] + nums[r] < x:
        l += 1
    else:
        r -= 1
print(answer)
 