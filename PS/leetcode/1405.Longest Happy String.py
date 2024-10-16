import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        result = []

        while pq:
            count1, char1 = heapq.heappop(pq)

            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                if not pq:
                    break 

                count2, char2 = heapq.heappop(pq)
                result.append(char2)
                count2 += 1  

                if count2 < 0:
                    heapq.heappush(pq, (count2, char2))

                heapq.heappush(pq, (count1, char1))
            else:
                result.append(char1)
                count1 += 1 

                if count1 < 0:
                    heapq.heappush(pq, (count1, char1))

        return ''.join(result)