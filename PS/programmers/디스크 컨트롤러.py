import heapq

def solution(jobs):
    start, end = -1, 0
    result = 0
    
    hq = []
    i = 0
    while i < len(jobs):
        # start와 end 사이에 있는 작업들을 heap에 넣어줌
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(hq, (job[1], job[0]))
        # 작업시간이 가장 작은 작업을 실행시킴
        if hq:
            current = heapq.heappop(hq)
            start = end
            end += current[0]
            result += end - current[1]
            i += 1
        else:
            end += 1
    return result // len(jobs)
            