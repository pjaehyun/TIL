import heapq

def change_heap(heap):
    for i in range(len(heap)):
        heap[i] *= -1
    return heap

def solution(operations):
    hq = []
    answer = []
    while operations:
        command, num = operations.pop(0).split()
        if command == 'I':
            heapq.heappush(hq, int(num))
        elif command == 'D':
            if hq:
                if num == '1':
                    # max heap
                    hq = change_heap(hq)
                    heapq.heapify(hq)
                    
                    heapq.heappop(hq)
                    
                    hq = change_heap(hq)
                    heapq.heapify(hq)
                else:
                    # min heap
                    heapq.heappop(hq)
                    
    for i in range(len(hq)):
        num = heapq.heappop(hq)
        if (num * -1) in answer:
            continue
        answer.append(num)
    
    if not answer:
        return [0,0]
    return [max(answer), min(answer)]