class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = True
        def isValid(arr):
            x = []
            nums = set()
            for val in arr:
                print(val)
                if val == '.':
                    x.append(val)
                else:
                    nums.add(val)
                print(nums)
            return 9 == len(nums) + len(x)

        for row in board:
            ans = ans and isValid(row)

        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])
            ans = ans and isValid(temp)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = []
                for x in range(3):
                    temp.append(board[i][j+x])
                    temp.append(board[i+1][j+x])
                    temp.append(board[i+2][j+x])
                ans = ans and isValid(temp)
        return ans

