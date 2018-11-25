class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.row = len(board)
        if self.row == 0:
            return []
        self.col = len(board[0])
        
        trie = {}
        for w in words:
            t = trie
            for i, c in enumerate(w):
                if c not in t:
                    t[c] = {}      
                t = t[c]
            t['is_word'] = True

        # print(trie)
        result = set()
        visited = [[False for _ in range(self.col)] for _ in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] in trie:
                    visited[i][j] = True
                    self.find_word(board, visited, i, j, board[i][j], result, trie[board[i][j]])
                    visited[i][j] = False 
        return list(result)
    
    def find_word(self, board, visited, i, j, current_word, result, trie):
        if 'is_word' in trie:
            result.add(current_word)

        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            x = dx + i
            y = dy + j
            if x >= 0 and x < self.row and y >= 0 and y < self.col and not visited[x][y] and board[x][y] in trie:
                visited[x][y] = True
                self.find_word(board, visited, x, y, current_word + board[x][y], result, trie[board[x][y]])
                visited[x][y] = False

# Another slightly different way:
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.row = len(board)
        if self.row == 0:
            return []
        self.col = len(board[0])
        
        trie = {}
        for w in words:
            t = trie
            for i, c in enumerate(w):
                if c not in t:
                    t[c] = {}      
                t = t[c]
            t['is_word'] = True
        result = set()
        visited = [[False for _ in range(self.col)] for _ in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                self.find_word(board, visited, i, j, "", result, trie)
        return list(result)
    
    def find_word(self, board, visited, i, j, current_word, result, trie):
        if 'is_word' in trie:
            result.add(current_word)
        if i >= self.row or i < 0 or j >= self.col or j < 0 or board[i][j] not in trie or visited[i][j]:
            return

        visited[i][j] = True
        self.find_word(board, visited, i, j + 1, current_word + board[i][j], result, trie[board[i][j]])
        self.find_word(board, visited, i + 1, j, current_word + board[i][j], result, trie[board[i][j]])
        self.find_word(board, visited, i, j - 1, current_word + board[i][j], result, trie[board[i][j]])
        self.find_word(board, visited, i - 1, j, current_word + board[i][j], result, trie[board[i][j]])

        visited[i][j] = False

