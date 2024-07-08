class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = [x for x in range(1, n+1)]
        curr_idx = 0

        while len(q) != 1:
            _next = (curr_idx + k - 1) % len(q)
            q.pop(_next)
            curr_idx = _next
        return q[0]
