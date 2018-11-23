class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """        
        self.dfs(board)

    def can_set(self, board, i, j, n):
        for k in range(9):
            if board[k][j] != '.' and board[k][j] == str(n):
                return False
            if board[i][k] != '.' and board[i][k] == str(n):
                return False
            if board[i // 3 * 3 + k //3][j // 3 * 3 + k % 3] != '.' and board[i // 3 * 3 + k //3][j // 3 * 3 + k % 3] == str(n):
                return False
        return True

    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for n in range(1, 10):
                        if self.can_set(board, i, j, n):
                            board[i][j] = str(n)
                            if self.dfs(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
