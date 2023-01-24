# 첫번째 풀이(2차원 배열로 풀이)
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        
        def get_coor(value):
            x = (value - 1) // n
            y = (value - 1) % n

            if x % 2 != 0:
                y = n - 1 - y
            return (x, y)
        
        def bfs(start):
            dq = deque()
            visited = set()

            dq.append((start, 0))
            visited.add(start)

            while dq:
                value, step = dq.popleft()
                if value == n**2:
                    return step

                for i in range(1, 7):
                    next = value + i
                    if next <= n**2:
                        x, y = get_coor(next)
                        
                        if board[x][y] != -1:
                            next = board[x][y]
                        if next not in visited:
                            dq.append((next, step+1))
                            visited.add(next)
        answer = bfs(1)
        if answer: return answer
        return -1

# 두번째 풀이(1차원 배열로 변경해서 풀이)
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        
        for i in range(len(board)):
            if i % 2 == 1:
                board[i] = board[i][::-1]
        
        board = list(chain.from_iterable(board))
        
        dq = deque()
        visited = set()

        dq.append((0, 0))
        while dq:
            value, step = dq.popleft()
            if value == n**2-1:
                return step
            for i in range(1, 7):
                new_val = value + i
                if new_val < n*n and new_val not in visited:
                    visited.add(new_val)
                    if board[new_val] == -1:
                        dq.append((new_val, step+1))
                    else:
                        dq.append((board[new_val]-1, step+1))
        return -1