class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        start = 0
        s = ' '.join(sentence) + ' '
        for i in range(rows):
            start += cols - 1
            if s[start % len(s)] == ' ':
                start += 1
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            else:
                while start > 0 and s[(start - 1) % len(s)] != ' ':
                    start -= 1
        
        return start // len(s)

