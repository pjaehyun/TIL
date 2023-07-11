# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.buildGraph(root)
        
        dq = deque()
        dq.append((target.val, 0))
        visited = set()

        visited.add(target.val)

        answer = []
        while dq:
            curr, dist = dq.popleft()
            if dist == k:
                answer.append(curr)
            for neib in self.graph[curr]:
                if neib not in visited:
                    visited.add(neib)
                    dq.append((neib, dist + 1))
        return answer

    def buildGraph(self, root):
        if not root:
            return
        if root.left:
            self.graph[root.val].append(root.left.val)
            self.graph[root.left.val].append(root.val)
        if root.right:
            self.graph[root.val].append(root.right.val)
            self.graph[root.right.val].append(root.val)
        self.buildGraph(root.left)
        self.buildGraph(root.right)
        
        

