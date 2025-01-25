class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        from collections import deque, defaultdict

        sorted_nums = sorted(nums)
        levels = defaultdict(deque)
        level_map = {}

        current_level = 0
        levels[current_level].append(sorted_nums[0])
        level_map[sorted_nums[0]] = current_level

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - levels[current_level][-1] <= limit:
                levels[current_level].append(sorted_nums[i])
            else:
                current_level += 1
                levels[current_level].append(sorted_nums[i])
            level_map[sorted_nums[i]] = current_level 

        for i in range(len(nums)):
            element_level = level_map[nums[i]] 
            nums[i] = levels[element_level].popleft()

        return nums