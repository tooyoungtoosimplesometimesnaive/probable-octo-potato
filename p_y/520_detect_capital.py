class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        first_capital = self.is_capital(word[0])
        count = 0
        for c in word:
            if self.is_capital(c):
                count += 1
        
        return count == 0 or count == len(word) or (first_capital and count == 1)
            
    def is_capital(self, c):
        return c >= 'A' and c <= 'Z'

