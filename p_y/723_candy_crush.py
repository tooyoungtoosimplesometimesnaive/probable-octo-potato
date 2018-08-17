class Solution:
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        while self.level(board):
            pass
        return board

    def move_down(self, board):
        rows = len(board)
        cols = len(board[0])
        for j in range(0, cols):
            p1 = rows - 1
            p2 = rows - 1
            while p2 >= 0:
                if board[p2][j] == 0:
                    p2 -= 1
                else:
                    board[p1][j] = board[p2][j]
                    p1 -= 1
                    p2 -= 1

            while p1 >= 0:
                board[p1][j] = 0
                p1 -= 1
    def level(self, board):
        rows = len(board)
        cols = len(board[0])
        mark_lists = []
        visited = [[False for i in range(0, cols)] for j in range(0, rows)]
        for i in range(0, rows):
            for j in range(0, cols):
                ml = []
                m, n = i, j
                val = board[i][j]
                if val == 0:
                    continue
                while m < rows and board[m][j] == val:
                    ml.append([m, j])
                    m += 1
                if len(ml) >= 3:
                    mark_lists.append(ml)

                ml = []
                while n < cols and board[i][n] == val:
                    ml.append([i, n])
                    n += 1

                #self.mark(board, i, j, visited, ml)
                if len(ml) >= 3:
                    mark_lists.append(ml)
        #print('------level------')
        #print(mark_lists)
        for l in mark_lists:
            for [a, b] in l:
                board[a][b] = 0
        #pretty_print(board)
        self.move_down(board)
        #print('-----after move down------')
        #pretty_print(board)

        if len(mark_lists) <= 0:
            return False
        return True

