class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dict_set = {}
        for word in set(dictionary):
            abbr_word = self.abbr(word)
            if abbr_word not in self.dict_set:
                self.dict_set[abbr_word] = word
            else:
                self.dict_set[abbr_word] = False
        # print(self.dict_set)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr_word = self.abbr(word)
        return abbr_word not in self.dict_set or (self.dict_set[abbr_word] == word)

    def abbr(self, word):
        return word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
