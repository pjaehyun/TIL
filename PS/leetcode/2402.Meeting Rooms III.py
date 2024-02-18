class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        booked = [i for i in range(n)]
        rooms = []
        res = [0] * n

        for s, e in meetings:
            while rooms and rooms[0][0] <= s:
                t, r = heapq.heappop(rooms)
                heapq.heappush(booked, r)
            if booked:
                r = heapq.heappop(booked)
                heapq.heappush(rooms, [e, r])
            else:
                t, r = heapq.heappop(rooms)
                heapq.heappush(rooms, [t+e-s, r])
            res[r] += 1
        return res.index(max(res))