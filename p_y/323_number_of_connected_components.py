class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        graph = self.build_graph(n, edges)
        
        number = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                q = [node]
                visited.add(node)
                number += 1
                while q:
                    top = q.pop(0)
                    for n in graph[top]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
                
        return number
        
    def build_graph(self, n, edges):
        def add_vertex(graph, v):
            if v not in graph:
                graph[v] = []
        def add_edge(graph, v1, v2):
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        graph = {}
        for i in range(n):
            add_vertex(graph, i)
        for v1, v2 in edges:
            add_edge(graph, v1, v2)
        
        return graph

