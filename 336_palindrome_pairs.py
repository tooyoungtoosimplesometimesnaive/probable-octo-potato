class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if words == None or len(words) == 0:
            return []

        words_map = {}
        for i, w in enumerate(words):
            words_map[w] = i
        
        result = []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                s1 = w[:j]
                s2 = w[j:]
                
                if self.is_palindrome(s1):
                    s2_rev = s2[::-1]
                    if s2_rev in words_map and words_map[s2_rev] != i:
                        result.append([words_map[s2_rev], i])
                if len(s2) > 0 and self.is_palindrome(s2):
                    s1_rev = s1[::-1]
                    if s1[::-1] in words_map and words_map[s1_rev] != i:
                        result.append([i, words_map[s1_rev]])
        
        return result
    def is_palindrome(self, w):
        i = 0
        j = len(w) - 1
        while i < j:
            if w[i] != w[j]:
                return False
            i += 1
            j -= 1
        return True

