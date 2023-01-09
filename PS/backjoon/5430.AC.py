# 문제 고려사항(이것들 때문에 삽질함..)
# 1. 배열을 뒤집을 때 시간복잡도 고려
# 2. n == 0 일 때 D연산이 없을 때 결과 출력(check로 판단안하고 arr이 비어있는지로 판단했기 때문)
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    command = input().strip()
    check = True
    reverse = 0
    n = int(input())

    arr = deque(input().strip()[1:-1].split(','))
    if n == 0:
        arr = []

    for i in range(len(command)):
        if command[i] == 'R':
            reverse += 1
        elif command[i] == 'D':
            if arr:
                if reverse % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                check = False
                break
    if check:
        if reverse % 2 != 0:
            arr.reverse()
        print('[' + ','.join(arr) + ']')    
