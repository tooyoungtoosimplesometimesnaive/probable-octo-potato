class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        i, j = 0, 0
        
        for m in moves:
            if m == 'U':
                j -= 1
            elif m == 'D':
                j += 1
            elif m == 'L':
                i -= 1
            elif m == 'R':
                i += 1
        
        return i == 0 and j == 0

