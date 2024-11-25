class Solution:
    def slidingPuzzle(self, board):
        dir = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        target = "123450"
        vis = set() 
        q = deque()
        start = ""

        for row in board:
            for col in row:
                start += str(col)

        q.append(start)
        vis.add(start)
        step = 0

        while q:
            size = len(q)
            for _ in range(size):
                current = q.popleft()

                if current == target:
                    return step

                zero = current.find('0') 
                for move in dir[zero]:
                    next_state = list(current)
                    next_state[zero], next_state[move] = next_state[move], next_state[zero]
                    next_state = ''.join(next_state)
                    if next_state not in vis: 
                        vis.add(next_state)
                        q.append(next_state)
            step += 1
        return -1 
