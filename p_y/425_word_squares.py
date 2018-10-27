class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def find_prefix(self, prefix):
        result = []
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return result
            curr = curr.children[c]
        
        self.dfs_search(curr, prefix, result)
        return result
    
    def dfs_search(self, node, w, result):
        if node.is_word:
            result.append(w)

        for k, v in node.children.items():
            self.dfs_search(v, w + k, result)

class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        result = []
        self.trie_tree = TrieTree()
        for w in words:
            self.trie_tree.insert(w)
    
        self.get_all(words, [], result)
        #print(result)
        return result

    def get_all(self, words, current, result):
        if len(current) == len(words[0]):
            result.append(current.copy())
            return
        prefix = self.get_prefix(current)
        next_level = self.trie_tree.find_prefix(prefix)
        for w in next_level:
            current.append(w)
            self.get_all(words, current, result)
            current.pop(-1)

    def get_prefix(self, current):
        level = len(current)
        prefix = ""
        for i in range(level):
            prefix += current[i][level]
        return prefix 

