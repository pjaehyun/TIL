class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        
        dq = deque()
        first = rooms[0]
        visited[0] = True
        for f in first:
            dq.append(f)
            visited[f] = True
        
        while dq:
            key = dq.popleft()
            for room in rooms[key]:
                if not visited[room]:
                    dq.append(room)
                    visited[room] = True
        return False if False in visited else True
