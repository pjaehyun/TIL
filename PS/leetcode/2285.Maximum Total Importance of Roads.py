class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = {x:0 for x in range(n)}
        for s, e in roads:
            count[s] += 1
            count[e] += 1
        
        rank = 1
        ranks = defaultdict(int)
        for k, v in sorted(count.items(), key=lambda x:(x[1], x[0])):
            ranks[k] = rank
            rank+=1
            
        answer = 0
        for s, e in roads:
            answer += ranks[s]
            answer += ranks[e]
        return answer