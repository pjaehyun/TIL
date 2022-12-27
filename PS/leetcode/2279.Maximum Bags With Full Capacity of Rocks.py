class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        answer = 0
        for i in range(len(capacity)):
            capacity[i] = capacity[i] - rocks[i]

        capacity.sort()
        for i in range(len(capacity)):
            if additionalRocks - capacity[i] >= 0:
                additionalRocks = additionalRocks - capacity[i]
                answer += 1
        return answer