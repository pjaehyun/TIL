class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        conn = {}
        has_ball = defaultdict(int)

        answer = [0] * len(queries)

        for i in range(len(queries)):
            x, y = queries[i]
            
            if x not in conn:
                conn[x] = y
            else:
                prev = conn[x]
                if has_ball[prev] == 1:
                    del has_ball[prev]
                else:
                    has_ball[prev] -= 1
                conn[x] = y
            
            has_ball[y] += 1
            answer[i] = len(has_ball)
        return answer
                