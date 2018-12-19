class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        queue = []
        N = len(board)
        queue.append(1)
        dist = {1:0}

        while queue:
            s = queue.pop(0)
            if s == N * N:
                # print(dist)
                return dist[s]
            
            for i in range(1,7):
                next_s = s + i
                if next_s <= N * N:
                    si, sj = self.get_coordinate(next_s, N)
                    next_s = board[si][sj] if board[si][sj] > 0 else next_s
                    if next_s not in dist:
                        dist[next_s] = dist[s] + 1
                        queue.append(next_s)
        return -1
                    
    def get_coordinate(self, s, N):
        a = (s - 1) // N
        row = N - a - 1
        b = (s - 1) % N
        col = b if row % 2 != N % 2 else N - 1 - b 
        return (row, col)

