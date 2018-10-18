class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word_map = collections.defaultdict(list)
        for i, w in enumerate(words):
            word_map[w].append(i)
        
        #print(word_map)
        i, j = 0, 0
        result = abs(word_map[word1][i] - word_map[word2][j])
        while i < len(word_map[word1]) and j < len(word_map[word2]):
            result = min(result, abs(word_map[word1][i] - word_map[word2][j]))
            if word_map[word1][i] < word_map[word2][j]:
                i += 1
            else:
                j += 1
        
        return result
