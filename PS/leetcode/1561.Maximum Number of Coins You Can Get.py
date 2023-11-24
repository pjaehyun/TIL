# 첫번째 풀이
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = deque(sorted(piles))
        answer = 0
        while piles:
            a = piles.pop()
            m = piles.pop()
            p = piles.popleft()

            answer += m
        return answer
    
# 두번째 풀이
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles)//3::2])