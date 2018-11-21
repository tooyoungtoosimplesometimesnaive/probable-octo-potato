class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        
        p = self.get_palindrome(s)
        last_index = [[] for _ in range(len(s))]
        
        for i in range(len(s)):
            for j in range(i + 1):
                if p[j][i]:
                    last_index[i].append(j - 1)
        #print(last_index)
        
        result = []
        self.construct(s, last_index, len(last_index) - 1, [], result) 
        return result

    def construct(self, s, last_index, index, current, result):
        if index == -1:
            result.append(current.copy())
            return
        for start in last_index[index]:
            current.insert(0, s[start + 1:index + 1])
            next_index = start
            self.construct(s, last_index, next_index, current, result)
            current.pop(0)
    
    def get_palindrome(self, s):
        p = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            p[i][i] = True
        # p[i][j] = p[i + 1][j - 1] if s[i] == s[j]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    p[i][j] = True
                elif j == i + 1:
                    p[i][j] = s[i] == s[j]
                else:
                    p[i][j] = p[i + 1][j - 1] if s[i] == s[j] else False
        
        return p

