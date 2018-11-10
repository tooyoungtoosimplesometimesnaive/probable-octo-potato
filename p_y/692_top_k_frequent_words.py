class WordFreq:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq.__lt__(other.freq)
        else:
            return self.word.__gt__(other.word)

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_count = collections.Counter()
        for w in words:
            words_count[w] += 1
        
        # Min heap
        pool = []
        for w, freq in words_count.items():
            heapq.heappush(pool, WordFreq(freq, w))
            if len(pool) == k + 1:
                heapq.heappop(pool)
        result = []
        while len(pool) > 0:
            result.insert(0, heapq.heappop(pool).word)
        return result
"""
from collections import defaultdict
from heapq import heappush, heappop

class WordFreq:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq.__lt__(other.freq)
        else:
            return self.word.__gt__(other.word)

class Solution:
    def topKFrequent(self, words, k):        
        # word frequency
        word_frequency = defaultdict(int)
        for word in words:
            word_frequency[word] += 1
        
        # current k most frequent elements
        k_most_frequent = []
        for word, freq in word_frequency.items():
            heappush(k_most_frequent, WordFreq(freq, word))
            if len(k_most_frequent) == k + 1:
                heappop(k_most_frequent)
        
        res = []
        while len(k_most_frequent) != 0:
            res.insert(0, heappop(k_most_frequent).word)
        
        return res
"""

