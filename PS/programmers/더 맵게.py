import heapq

def solution(scoville, K):
    result = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        result += 1
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        new_scoville = a + (b * 2)
        heapq.heappush(scoville, new_scoville)
    return result
        