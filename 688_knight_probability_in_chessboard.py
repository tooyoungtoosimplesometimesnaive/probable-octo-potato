class Solution:
    def __init__(self):
        self.dirs = [[1, 2], 
                     [1, -2], 
                     [-1, 2], 
                     [-1, -2], 
                     [2, 1], 
                     [2, -1],
                     [-2, 1],
                     [-2, -1]
                    ]
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        board = [[0 for _ in range(N)] for _ in range(N)]
        board[r][c] = 1
        for k in range(K):
            tmp = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if board[i][j] > 0:
                        for dx, dy in self.dirs:
                            x = i + dx
                            y = j + dy
                            if x >= 0 and x < N and y >= 0 and y < N:
                                tmp[x][y] += board[i][j]
            board = tmp
            #print(board)
        result = 0
        for i in range(N):
            for j in range(N):
                result += board[i][j]

        return result / (8 ** K)

