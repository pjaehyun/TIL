from collections import deque
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.memLim = memoryLimit
        self.q = deque()
        self.s = set()
        self.d = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.s:
            return False
        self.q.append(key)
        self.s.add(key)
        if destination not in self.d:
            self.d[destination] = [[], 0]
        self.d[destination][0].append(timestamp)
        if len(self.q) > self.memLim:
            u, v, t = self.q.popleft()
            self.s.remove((u, v, t))
            ts, l = self.d[v]
            self.d[v][1] = l + 1
        return True

    def forwardPacket(self) -> list[int]:
        if not self.q:
            return []
        u, v, t = self.q.popleft()
        self.s.remove((u, v, t))
        ts, l = self.d[v]
        self.d[v][1] = l + 1
        return [u, v, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.d:
            return 0
        ts, l = self.d[destination]
        if l >= len(ts):
            return 0
        return max(0, bisect_right(ts, endTime, l) - bisect_left(ts, startTime, l))