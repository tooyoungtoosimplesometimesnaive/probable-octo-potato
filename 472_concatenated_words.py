class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words_set = set()
        def qualified(word):
            if word in words_set:
                return True
            for i in range(1, len(word)):
                if word[:i] in words_set and qualified(word[i:]):
                    return True
            return False
        
        words = sorted(words, key=lambda w: len(w))
        result = []
        for word in words:
            if qualified(word):
                result.append(word)
            words_set.add(word)
        
        return result

