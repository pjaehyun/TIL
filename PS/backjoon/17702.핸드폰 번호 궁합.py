import sys
input = sys.stdin.readline

A = list(map(int, input().strip()))
B = list(map(int, input().strip()))
arr = [0]*16
for i in range(16):
    if i % 2 == 0:
        arr[i] = A[i//2]
    else:
        arr[i] = B[i//2]

while len(arr) != 2:
    temp = []
    for i in range(len(arr)-1):
        num = (arr[i]+arr[i+1]) % 10
        temp.append(num)
    arr = temp

print(*arr, sep="")