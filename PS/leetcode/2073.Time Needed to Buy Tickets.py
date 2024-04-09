class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(list(enumerate(tickets)))
        
        time = 0
        while tickets:
            idx, ticket = tickets.popleft()
            
            ticket -= 1
            if idx == k and ticket == 0:
                return time + 1

            if ticket > 0:
                tickets.append((idx, ticket))

            time += 1
        return time