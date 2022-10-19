class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1 if (i == 0) or (i == x-1) else 0 for i in range(x)] for x in range(1, numRows+1)]
        for i in range(len(pascal)):
            for j in range(len(pascal[i])):
                if pascal[i][j] == 0:
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal