class Solution:
    def clearStars(self, s: str) -> str:
        
        hq = []
        smallest = defaultdict(list)

        for i in range(len(s)):
            if s[i] == "*":
                asc = heapq.heappop(hq)
                c = chr(asc)
                smallest[c].pop()
                continue
            heapq.heappush(hq, ord(s[i]))
            smallest[s[i]].append(i)

        answer = [""] * len(s)
        
        for k, v in smallest.items():
            for i in v:
                answer[i] = k
        return ''.join(answer)