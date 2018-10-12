class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        parent_map = {}
        level_map = {}
        parent_map[beginWord] = []
        level_map[beginWord] = 0
        
        queue = []
        queue.append(beginWord)
        level = 0
        while len(queue) > 0:
            for k in range(len(queue)):
                curr_word = queue.pop(0)
                for i in range(len(curr_word)):
                    curr_char = curr_word[i]
                    for ch_id in range(26):
                        new_char = chr(ord('a') + ch_id)
                        if curr_char != new_char:
                            next_word = list(curr_word)
                            next_word[i] = new_char
                            next_word = ''.join(next_word)
                            if next_word in word_set and next_word not in level_map:
                                parent_map[next_word] = []
                                parent_map[next_word].append(curr_word)
                                level_map[next_word] = level + 1
                                queue.append(next_word)
                            elif next_word in word_set and level + 1 == level_map[next_word]:
                                parent_map[next_word].append(curr_word)
            if endWord in level_map:
                break
            level += 1

        #print(parent_map)
        results = []
        #print('----')
        def dfs(parent_map, end, start, path):

            path.append(end)
            if len(parent_map[end]) == 0:
                results.append(path[::-1].copy())
            else:
                for n in parent_map[end]:
                    dfs(parent_map, n, start, path)
            path.pop(-1)

        if endWord not in parent_map:        
                return []
        dfs(parent_map, endWord, beginWord, [])
        
        #print(results)
        return results
        
         
