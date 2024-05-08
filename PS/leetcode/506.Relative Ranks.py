class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [(-value, idx) for idx, value in enumerate(score)]
        heapq.heapify(score)
        
        answer = [None] * len(score)
        seq = 1
        while score:
            value, idx = heapq.heappop(score)
            if seq == 1:
                answer[idx] = "Gold Medal"
            elif seq == 2:
                answer[idx] = "Silver Medal"
            elif seq == 3:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(seq)
            seq += 1
        return answer
            
            