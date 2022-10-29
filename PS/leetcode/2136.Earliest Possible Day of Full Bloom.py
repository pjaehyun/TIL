class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        min_grow = 0
        result = 0
        for plant, grow in reversed(sorted(zip(plantTime, growTime), key=lambda x:x[1])):
            result = max(result, min_grow + plant + grow)
            min_grow += plant
        return result