class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1] * len(queries)
        new_queries = [[] for _ in range(len(heights))]
        mono_stack = []
        
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a 
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                new_queries[b].append((heights[a], i))

        for i in range(len(heights) - 1, -1, -1):
            for height_a, idx in new_queries[i]:
                pos = self.binary_search(height_a, mono_stack)
                if pos != -1:
                    result[idx] = mono_stack[pos][1]
            
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))
        
        return result

    def binary_search(self, height: int, mono_stack: List[tuple]) -> int:
        left, right = 0, len(mono_stack) - 1
        best_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] > height:
                best_pos = mid
                left = mid + 1
            else:
                right = mid - 1
        return best_pos