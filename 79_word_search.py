# This got TLE
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.row = len(board)
        self.col = len(board[0])
        
        visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if self.find(board, visited, word, i, j, 0):
                    return True
        return False
    
    def find(self, board, visited, word, i, j, current_index):
        if current_index == len(word):
            return True
        if i >= self.row or i<0 or j>=self.col or j<0 or visited[i][j] or board[i][j] != word[current_index]:
            return False
        visited[i][j] = True
        a = self.find(board, visited, word, i + 1, j, current_index + 1)
        b = self.find(board, visited, word, i - 1, j, current_index + 1)
        c = self.find(board, visited, word, i, j + 1, current_index + 1)
        d = self.find(board, visited, word, i, j - 1, current_index + 1)
        visited[i][j] = False
        return a or b or c or d

# This is OK:
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.row = len(board)
        self.col = len(board[0])

        # visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if self.find(board, word, i, j, 0):
                    return True
        return False

    def find(self, board, word, i, j, current_index):
        if current_index == len(word):
            return True
        if i >= self.row or i<0 or j>=self.col or j<0 or board[i][j] != word[current_index]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        a = self.find(board, word, i + 1, j, current_index + 1) or self.find(board, word, i - 1, j, current_index + 1) \
            or self.find(board, word, i, j + 1, current_index + 1) or self.find(board, word, i, j - 1, current_index + 1)
        board[i][j] = tmp
        return a

