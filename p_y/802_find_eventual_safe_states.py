class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        result = []
        visited = [0 for _ in range(len(graph))]

        for node in range(len(graph)):
            if self.is_valid(graph, visited, node):
                result.append(node)
        return result
        
    def is_valid(self, graph, visited, node):
        if visited[node] != 0:
            return visited[node] == 2

        visited[node] = 1

        for n in graph[node]:
            if visited[n] == 2:
                continue
            if visited[n] == 1 or not self.is_valid(graph, visited, n):
                return False
        visited[node] = 2
        return True

