class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        events = []
        for num in nums:
            events.append((num - k, 1)) 
            events.append((num + k + 1, -1))

        events.sort()

        max_beauty = 0
        current_count = 0
        for value, effect in events:
            current_count += effect
            max_beauty = max(max_beauty, current_count)

        return max_beauty