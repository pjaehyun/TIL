class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        numRows = len(rowSum)
        numCols = len(colSum)
        result = [[0] * numCols for _ in range(numRows)]

        i, j = 0, 0

        while i < numRows and j < numCols:
            val = min(rowSum[i], colSum[j])
            result[i][j] = val
            rowSum[i] -= val
            colSum[j] -= val

            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        
        return result
        