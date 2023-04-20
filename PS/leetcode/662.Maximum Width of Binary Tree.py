# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        dq = deque([(root, 1)])
        answer = 0
        while dq:
            temp = []
            for i in range(len(dq)):
                curr, idx = dq.popleft()
                temp.append(idx)
                if curr.left:
                    if idx > 1:
                        dq.append((curr.left, idx*2-1))    
                    else: dq.append((curr.left, idx*1))
                    
                
                if curr.right:
                    dq.append((curr.right, idx*2))
            answer = max(answer, max(temp) - min(temp) + 1)
        return answer