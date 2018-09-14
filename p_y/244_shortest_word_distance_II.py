class WordDistance:

    m = {}
    l = 0
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.l = len(words)
        self.m = collections.defaultdict(list)
        for i in range(len(words)):
            self.m[words[i]].append(i)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_ids = self.m[word1]
        word2_ids = self.m[word2]
        result = self.l
        
        j, k = 0, 0
        while j < len(word1_ids) and k < len(word2_ids):
            result = min(result, abs(word1_ids[j] - word2_ids[k]))
            if word1_ids[j] > word2_ids[k]:
                k = k + 1
            else:
                j = j + 1
#         for i in word1_ids:
#             for j in word2_ids:
#                 result = min(result, abs(i - j))
        
        return result
