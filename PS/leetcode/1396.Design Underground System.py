class UndergroundSystem:

    def __init__(self):
        self.info = defaultdict(list)
        self.average = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.info[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        dist = t - self.info[id][1]
        self.average[self.info[id][0] + '#' + stationName].append(dist)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.average[startStation+ '#' +endStation]) / len(self.average[startStation+ '#' +endStation])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)