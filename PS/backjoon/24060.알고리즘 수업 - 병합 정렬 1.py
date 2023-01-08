import sys
sys.setrecursionlimit(10000000)

input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))
answer = []

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    devide = (len(arr)+1) // 2
    left = merge_sort(arr[:devide])
    right = merge_sort(arr[devide:])

    merged = []
    l, r = 0, 0

    while len(left) > l and len(right) > r:
        if left[l] > right[r]:
            merged.append(right[r])
            r += 1
        else:
            merged.append(left[l])
            l += 1
    
    while len(left) > l:
        merged.append(left[l])
        l += 1
    
    while len(right) > r:
        merged.append(right[r])
        r += 1
    i = 0
    while i < len(merged):
        answer.append(merged[i])
        i += 1
    return merged

merge_sort(arr)
if K > len(answer): print(-1)
else: print(answer[K-1])
