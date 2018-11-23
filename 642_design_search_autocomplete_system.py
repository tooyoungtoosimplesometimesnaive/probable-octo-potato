class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.keyword = ""
        self.root = TrieNode()
        for sentence, time in zip(sentences, times):
            self.add_record(sentence, time)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        result = []
        if c != '#':
            self.keyword += c
            result = self.search_trie(self.keyword)
        else:
            self.add_record(self.keyword, 1)
            self.keyword = ""
        
        return [item[1] for item in sorted(result)[:3]]
        
        
        
    def add_record(self, sentence, time):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isEnd = True
        p.data = sentence
        # For Easy sort
        p.rank -= time
    
    def dfs(self, root):
        result = []
        if root == None:
            return []
        if root.isEnd:
            result.append((root.rank, root.data))
        for child in root.children:
            result = result + self.dfs(root.children[child])
        return result
    
    def search_trie(self, sentence):
        p = self.root
        for c in sentence:
            if c not in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
