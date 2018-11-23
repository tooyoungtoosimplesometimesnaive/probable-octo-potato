class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.map = {}
        for weight, w in enumerate(words):
            for i in range(len(w) + 1):
                for j in range(len(w) + 1):
                    self.map[w[:i] + '#' + w[len(w) - j:]] = weight
        
        # print(self.map)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return -1 if prefix + '#' + suffix not in self.map else self.map[prefix + '#' + suffix]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

