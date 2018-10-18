class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            ids = []
            for i, w in enumerate(words):
                if word1 == w:
                    ids.append(i)
            if len(ids) == 1:
                return 0
            i = 0
            j = 1
            result = ids[j] - ids[i]
            while j < len(ids):
                result = min(result, ids[j] - ids[i])
                j += 1
                i += 1
            return result
        else:
            word1_ids = []
            word2_ids = []
            for i, w in enumerate(words):
                if w == word1: word1_ids.append(i)
                if w == word2: word2_ids.append(i)
            result = abs(word1_ids[0] - word2_ids[0])
            i = 0
            j = 0
            while i < len(word1_ids) and j < len(word2_ids):
                result = min(result, abs(word1_ids[i] - word2_ids[j]))
                if word1_ids[i] < word2_ids[j]:
                    i += 1
                else:
                    j += 1
            return result
