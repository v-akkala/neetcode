class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        rows = set()
        cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        zerorow = [0] * len(matrix[0])
        for row in rows:
            matrix[row] = zerorow
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
