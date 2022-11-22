class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees
        # check turn left or turn right
        def ccw(A, B, C):
            return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
        
        # Convex Hull Algorithm(Monotone Chain)
        trees.sort()
        
        stack = []
        for i in chain(range(len(trees)), reversed(range(len(trees)-1))):
            while len(stack) >= 2 and ccw(stack[-2], stack[-1], trees[i]) < 0:
                stack.pop()
            stack.append(trees[i])
        stack.pop()

        for i in range(1, (len(stack)+1)//2):
            if stack[i] != stack[-1]:
                break
            stack.pop()
        return stack
