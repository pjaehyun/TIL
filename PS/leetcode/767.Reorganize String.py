# 스택으로 풀이 실패 
# 다른사람 어떻게 풀었는지 보고 이해 후 다시 풀이
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        
        max_heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(max_heap)

        answer = []

        while len(max_heap) >= 2:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)

            answer.extend([char1, char2])

            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))
            
        if max_heap:
            count, char = heapq.heappop(max_heap)
            if -count > 1:
                return ""
            answer.append(char)
        return ''.join(answer)