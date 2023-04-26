import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


N = int(input())

inorder, postorder = list(map(int, input().split())), list(map(int, input().split()))

i = len(inorder) - 1
p = len(postorder) - 1

stack = []
prev = None

root = TreeNode(postorder[p])
p -= 1

stack.append(root)

while p >= 0:
    while stack and stack[-1].val == inorder[i]:
        prev = stack.pop()
        i -= 1
    new_node = TreeNode(postorder[p])
    if prev:
        prev.left = new_node
    elif stack:
        cur = stack[-1]
        cur.right = new_node
    stack.append(new_node)
    prev = None
    p -= 1

answer = []
def preorder(root):
    if not root:
        return
    
    answer.append(str(root.val))
    preorder(root.left)
    preorder(root.right)
preorder(root)
print(' '.join(answer))