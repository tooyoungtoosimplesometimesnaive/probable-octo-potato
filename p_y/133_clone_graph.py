# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visited = dict()
        return self.clone(node, visited)
    
    def clone(self, node, visited):
        new_node = None
        if node == None:
            return new_node
        if node not in visited:
            new_node = UndirectedGraphNode(node.label)
            visited[node] = new_node
        else:
            new_node = visited[node]
            return new_node

        for n in node.neighbors:
            new_n = self.clone(n, visited)
            new_node.neighbors.append(new_n)
        
        return new_node

