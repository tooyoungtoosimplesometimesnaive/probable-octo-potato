class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                count = 0
                if i - 1 >= 0:
                    count += self.get_value(board[i - 1][j])
                if i + 1 < row:
                    count += self.get_value(board[i + 1][j])
                if j - 1 >= 0:
                    count += self.get_value(board[i][j - 1])
                if j + 1 < col:
                    count += self.get_value(board[i][j + 1])
                if i - 1 >= 0 and j - 1 >= 0:
                    count += self.get_value(board[i - 1][j - 1])
                if i - 1 >= 0 and j + 1 < col:
                    count += self.get_value(board[i - 1][j + 1])
                if i + 1 < row and j - 1 >= 0:
                    count += self.get_value(board[i + 1][j - 1])
                if i + 1 < row and j + 1 < col:
                    count += self.get_value(board[i + 1][j + 1])
                # 2 : meaning live -> die
                # 3 : meaning die -> live
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 2
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3

        for i in range(row):
            for j in range(col):
                if board[i][j] == 3:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0

    def get_value(self, v):
        if v == 2 or v == 1:
            return 1
        else:
            return 0
