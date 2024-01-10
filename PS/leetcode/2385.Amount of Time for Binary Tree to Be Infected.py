# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if not node:
                return

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        graph = defaultdict(list)
        dfs(root)
        visited = set()
        dq = deque([start])
        time = -1
        while dq:
            time += 1
            for _ in range(len(dq)):
                curr = dq.popleft()
                visited.add(curr)
                for neib in graph[curr]:
                    if neib not in visited:
                        dq.append(neib)
        return time