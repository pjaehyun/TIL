# 완전탐색
def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer


# 큐
from collections import deque
def solution(prices):
    answer = []
    dq = deque(prices)
    while dq:
        price = dq.popleft()
        count = 0
        for num in dq:
            count += 1
            if price > num:
                break
        answer.append(count)
    return answer


# 스택(시간복잡도 가장 우위)
from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            idx, price = stack.pop()
            answer[idx] = i - idx
        stack.append((i, prices[i]))
    for idx, price in stack:
        answer[idx] = len(prices) - idx - 1
    return answer
            