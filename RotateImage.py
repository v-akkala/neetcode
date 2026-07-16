class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s = 1
        i = 0
        l = len(matrix)
        while s < l:
            matrix[i].reverse()
            j = l - s - 1
            b = 1
            while j >= 0:
                matrix[i][j], matrix[i + b][i] = matrix[i + b][i], matrix[i][j]
                b += 1
                j -= 1
            s += 1
            i += 1
        matrix[l - 1].reverse()
