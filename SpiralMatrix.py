class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        l = len(matrix) * len(matrix[0])
        visited = {(0, 0)}
        r, c = 0, 0
        ans.append(matrix[0][0])
        while len(ans) != l:
            while c + 1 < len(matrix[0]) and (r, c + 1) not in visited:
                c += 1
                visited.add((r, c))
                ans.append(matrix[r][c])
            while r + 1 < len(matrix) and (r + 1, c) not in visited:
                r += 1
                visited.add((r, c))
                ans.append(matrix[r][c])
            while c - 1 >= 0 and (r, c - 1) not in visited:
                c -= 1
                visited.add((r, c))
                ans.append(matrix[r][c])
            while r - 1 >= 0 and (r - 1, c) not in visited:
                r -= 1
                visited.add((r, c))
                ans.append(matrix[r][c])
        return ans
