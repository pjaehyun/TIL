# 첫번째 풀이
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        pascal = [[1],[1,1]]

        for i in range(rowIndex-1):
            pascal.append([1] + [pascal[-1][j] + pascal[-1][j+1] for j in range(i+1)] + [1])
        return pascal[rowIndex]


# 두번째 풀이
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1 if (i == 0) or (i == x) else 0 for i in range(x+1)] for x in range(rowIndex + 1)]
        for i in range(len(pascal)):
            for j in range(len(pascal[i])):
                if pascal[i][j] == 0:
                    print(i,j)
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal[rowIndex]