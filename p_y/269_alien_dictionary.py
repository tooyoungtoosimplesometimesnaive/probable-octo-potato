class Solution:
    def __init__(self):
        self.graph = {}
        self.indegree = {}
    
    def add_edge(self, v1, v2): # v1 -> v2
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.graph[v1].append(v2)
        self.indegree[v2] += 1
        
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
        if v not in self.indegree:
            self.indegree[v] = 0
        
    def build_graph(self, words):
        if len(words) == 0: return
        if len(words) == 1:
            for i in words[0]:
                self.add_vertex(i)
        
        i = 0
        j = 1
        while j < len(words):
            w1 = words[i]
            w2 = words[j]
            for c in w1: self.add_vertex(c)
            for c in w2: self.add_vertex(c)

            wid = 0 # word index
            while wid < len(w1) and wid < len(w2):
                if w1[wid] != w2[wid]:
                    self.add_edge(w1[wid], w2[wid])
                    break
                wid += 1

            j += 1
            i += 1
        
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.build_graph(words)

        result = []
        zero_indegree = list({k for k, v in self.indegree.items() if v == 0})
        while zero_indegree:
            v = zero_indegree.pop(0)
            result.append(v)
            for n in self.graph[v]:
                self.indegree[n] -= 1
                if self.indegree[n] == 0:
                    zero_indegree.append(n)
        
        return ''.join(result) if len(result) == len(self.graph) else ""

