# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 첫번째 풀이
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        dq = deque([(root, 0)])
        tree = defaultdict(list)

        while dq:
            curr, level = dq.popleft()
            if level % 2 != 0:
                if curr.val % 2 != 0:
                    return False
                if tree[level] and curr.val >= tree[level][-1]:
                    return False
            
            if level % 2 == 0:
                if curr.val % 2 == 0:
                    return False
                if tree[level] and curr.val <= tree[level][-1]:
                    return False
            tree[level].append(curr.val)
            if curr.left:
                dq.append((curr.left, level + 1))
            
            if curr.right:
                dq.append((curr.right, level + 1))
        return True

# 두번째 풀이
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        dq = deque([root])
        level = 0
        while dq:
            prev = float('-inf') if level % 2 == 0 else float('inf')
            for _ in range(len(dq)):
                curr = dq.popleft()
                if (level % 2 == 0 and (curr.val % 2 == 0 or curr.val <= prev)) or (level % 2 != 0 and (curr.val % 2 != 0 or curr.val >= prev)):
                    return False
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
                prev = curr.val
            level += 1
        return True