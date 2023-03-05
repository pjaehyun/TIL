import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
prefixSum = arr[0]
answer = float('inf')
while True:
    if prefixSum >= S:
        prefixSum -= arr[left]
        answer = min(answer, right - left + 1)
        left += 1
    else:
        right += 1
        if right == N: break
        prefixSum += arr[right]
if answer != float('inf'):
    print(answer)
else:
    print(0)