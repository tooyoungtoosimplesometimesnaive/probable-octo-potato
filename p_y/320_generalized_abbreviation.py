class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def get_abbr(word, start, current_word, current_count, results):
            """"""
            if start >= len(word):
                results.append(current_word)
                return
            
            get_abbr(word, start + 1, current_word + word[start], 0, results)
            
            while len(current_word) > 0 and current_word[-1] >= '0' and current_word[-1] <= '9':
                current_word = current_word[:-1]
            get_abbr(word, start + 1, current_word + str(current_count + 1), current_count + 1, results)
        
        results = []
        get_abbr(word, 0, "", 0, results)
        return results
            
