class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [0 for _ in range(9)]
        col = [0 for _ in range(9)]
        block = [0 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = 1 << int(board[i][j])
                    if (col[j] & num) or (row[i] & num) or (block[i // 3 * 3 + j // 3] & num):
                        return False
                    
                    row[i] |= num
                    col[j] |= num
                    block[i//3*3 + j//3] |= num
        return True

