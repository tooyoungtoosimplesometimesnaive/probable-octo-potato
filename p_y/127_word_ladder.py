class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        visited = set()
        queue = []
        queue.append(beginWord)
        level = 1
        while len(queue) > 0:
            for k in range(len(queue)):
                curr = queue.pop(0)
                for i in range(len(curr)):
                    curr_ch = curr[i]
                    for char_i in range(26):
                        char = chr(ord('a') + char_i)
                        if char != curr_ch:
                            next_word = list(curr)
                            next_word[i] = char
                            next_word = "".join(next_word)
                        
                            if next_word not in visited and next_word in wordSet:
                                if next_word == endWord:
                                    return level + 1
                                queue.append(next_word)
                                visited.add(next_word)
            level += 1
        return 0

