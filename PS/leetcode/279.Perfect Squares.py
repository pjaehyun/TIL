# Dp 풀이 방식
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf for _ in range(10001)]
        dp[0] = 0
        ps = []
        
        i = 1
        while i*i <= n:
            ps.append(i*i)
            i += 1
        
        for i in range(1, n + 1):
            for s in ps:
                if i < s:
                    break
                dp[i] = min(dp[i], dp[i-s] + 1)  
        return dp[n]


# Bfs 풀이 방식
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n

        perfect_square = []
        i = 1
        while i * i <= n:
            perfect_square.append(i*i)
            i += 1
        
        check = {n}
        count = 0
        while check:
            count += 1
            temp = set()
            for num in check:
                for square in perfect_square:
                    if num == square:
                        return count
                    if num < square:
                        break
                    temp.add(num - square)
            check = temp
        return count