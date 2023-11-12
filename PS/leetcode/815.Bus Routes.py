class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        station = defaultdict(list)

        if source == target:
            return 0

        for i in range(len(routes)):
            for s in routes[i]:
                station[s].append(i)
        dq = deque([(source, 0)])
        visited_station = set([source])
        visited_bus = set()
        
        while dq:
            curr, transfer = dq.popleft()
            if curr == target:
                return transfer
            
            for bus in station[curr]:
                if bus not in visited_bus:
                    visited_bus.add(bus)

                    for s in routes[bus]:
                        if s not in visited_station:
                            visited_station.add(s)
                            dq.append((s, transfer + 1))

        return -1