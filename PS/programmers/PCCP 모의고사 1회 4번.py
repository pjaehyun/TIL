# 총 소요시간 40분
# 시간 초과 해결책 찾느라 오래 걸림(프로그램을 일반 리스트에서 deque로 변환하니 시간 초과 해결)
import heapq
from collections import deque

def solution(program):
    hq = []
    
    start, end = -1, 0
    answer = [0] * 11
    i = 0
    program.sort(key=lambda x:(x[1], x[0]))
    program = deque(program)
    n = len(program)
    while i < n:
        while program and start < program[0][1] <= end:
            heapq.heappush(hq, program.popleft())
        if hq:
            curr = heapq.heappop(hq)
            answer[curr[0]] += (end - curr[1])
            start = end
            end += curr[2]
            i += 1
        else:
            end += 1
    answer[0] = end
    return answer