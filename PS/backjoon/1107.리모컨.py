import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
error = list(map(str, input().split()))

answer = abs(100 - N)

for nums in range(1000001):
    nums = str(nums)
    
    for i in range(len(nums)):
        if nums[i] in error:
            break
        elif i+1 == len(nums):
            answer = min(answer, abs(int(nums) - N) + len(nums))
print(answer)
            