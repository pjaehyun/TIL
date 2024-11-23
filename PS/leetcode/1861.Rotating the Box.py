class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        for i in range(m):
            count = 0
            start_idx = -1
            for j in range(n):
                if box[i][j] == '#':
                    count += 1
                elif box[i][j] == '*':
                    for k in range(j - 1, start_idx, -1):
                        if count > 0:
                            box[i][k] = '#'
                            count -= 1
                        else:
                            box[i][k] = '.'
                    start_idx = j
            for k in range(n - 1, start_idx, -1):
                if count > 0:
                    box[i][k] = '#'
                    count -= 1
                else:
                    box[i][k] = '.'
                

        res = [["."] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if box[i][j] == '#':
                    res[j][m-1-i] = '#'
                elif box[i][j] == '*':
                    res[j][m-1-i] = '*'
        return res