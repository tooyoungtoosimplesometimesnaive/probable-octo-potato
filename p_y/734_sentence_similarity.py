class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        d = collections.defaultdict(set)
        for pair in pairs:
            d[pair[0]].add(pair[1])
            d[pair[1]].add(pair[0])

        count = 0

        id = 0
        for word in words1:
            if word == words2[id]:
                count += 1
            elif word in d:
                pSet = d[word]
                if words2[id] in pSet:
                    count += 1
            id += 1
        return count == len(words1)

