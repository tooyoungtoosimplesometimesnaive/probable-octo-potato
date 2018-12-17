# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
            
            # use the least number of 0 matches word as the word to guess. which means the highest possibility
            mini = min(wordlist, key=lambda x : count[x])
            
            n = master.guess(mini)
            
            wordlist = [w for w in wordlist if self.match(mini, w) == n]
    
    
    
    def match(self, w1, w2):
        result = 0
        for i in range(6):
            if w1[i] == w2[i]:
                result += 1
        return result

