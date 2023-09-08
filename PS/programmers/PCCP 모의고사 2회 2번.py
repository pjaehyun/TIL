# 제출 코드
import heapq

def solution(ability, number):
    heapq.heapify(ability)
    
    for _ in range(number):
        recruit1 = heapq.heappop(ability)
        recruit2 = heapq.heappop(ability)

        recruit1 += recruit2

        heapq.heappush(ability, recruit1)
        heapq.heappush(ability, recruit1)
    
    return sum(ability)

# 종료 후 리팩토링
import heapq

def solution(ability, number):
    heapq.heapify(ability)
    
    for _ in range(number):
        fusion = 0
        for _ in range(2):
            fusion += heapq.heappop(ability)

        heapq.heappush(ability, fusion)
        heapq.heappush(ability, fusion)
    return sum(ability)