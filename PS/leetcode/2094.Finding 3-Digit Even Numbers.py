class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        def bt(x, num):
            if len(num) >= 3:
                x = num[0] * 100 + num[1] * 10 + num[2]
                if 100 <= x < 1000 and x % 2 == 0 and distinct_num[x] <= 0:
                    answer.append(x)
                    distinct_num[x] += 1
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    bt(i, num + [digits[i]])
                    visited[i] = False

        visited = [False] * n
        distinct_num = defaultdict(int)
        answer = []
        for i in range(n):
            visited[i] = True
            bt(i, [digits[i]])
            visited[i] = False
        answer.sort()
        return answer