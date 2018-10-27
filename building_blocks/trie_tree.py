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


if __name__ == '__main__':
    t = TrieTree()

    for w in ["ulus","mity","wind","chip","pill","pugh","flux","crib","sump","piss","fils","high","pipy","rusk","cuss","miri","pung","this","knit","hisn","zins","puns","tuff","ruth","whit","wild","burd","hubs","grin","kirs","zips","migg","lump","dint","jiff","spud","pith","rill","twit","pugs","ichs","jugs","simp","crus"]:
        t.insert(w);
    print(t.find_prefix("mi"))
    #print(t.find_prefix(""))
