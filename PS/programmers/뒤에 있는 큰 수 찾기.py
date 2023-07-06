from collections import deque
def solution(numbers):
    dq = deque([(idx, v) for idx, v in enumerate(numbers)])

    stack = []
    answer = [-1] * len(numbers)
    
    while dq:
        i, v = dq.popleft()
        
        while stack and stack[-1][1] < v:
            e = stack.pop()
            answer[e[0]] = v
        stack.append((i, v))
    return answer
    