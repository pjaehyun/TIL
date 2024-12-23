
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps_to_sort(arr: List[int]) -> int:
            n = len(arr)
            indexed_arr = [(val, i) for i, val in enumerate(arr)]
            indexed_arr.sort()  
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or indexed_arr[i][1] == i:
                    continue

                cycle_size = 0
                x = i

                while not visited[x]:
                    visited[x] = True
                    x = indexed_arr[x][1]
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        queue = deque([root])
        total_swaps = 0

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total_swaps += min_swaps_to_sort(current_level)

        return total_swaps