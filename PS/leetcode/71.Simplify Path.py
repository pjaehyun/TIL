class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = deque(path.split('/'))

        stack = []

        while paths:
            path = paths.popleft()
            if path == "":
                continue
            elif path != '..' and path != '.':
                stack.append(path)
            elif stack and path == '..':
                stack.pop()
            
        return '/' + '/'.join(stack)
