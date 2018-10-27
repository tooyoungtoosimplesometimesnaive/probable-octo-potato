class Solution:
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        col = len(words[0])
        row = len(words)
        
        if col != row:
            return False
        
        for i in range(1, row):
            if len(words[i - 1]) < len(words[i]):
                return False
        
        for i in range(row):
            w = words[i]
            r = words[i][i:]
            k = i
            l = ""
            while k < row:
                if i >= len(words[k]):
                    break
                l += words[k][i]
                k += 1
            if l != r:
                return False
                
        return True

