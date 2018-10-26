class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def other_level(l):
            return 0 if l == 1 else 1
        state = [-1 for _ in range(len(graph))]
        
        for i in range(len(graph)):
            if state[i] != -1:
                continue
            q = [i]
            level = 0
            while q:
                for _ in range(len(q)):
                    top = q.pop(0)
                    if state[top] == -1:
                        state[top] = level % 2
                        
                    for n in graph[top]:
                        if state[n] == -1:
                            q.append(n)
                level += 1
        
        for i in range(len(graph)):
            for n in graph[i]:
                if state[i] == state[n]:
                    return False
        
        return True

# DFS method:
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        state = [-1 for _ in range(len(graph))]

        for i in range(len(graph)):
            if state[i] == -1 and not self.valid_color(graph, state, i, 0):
                return False
        return True

    def valid_color(self, graph, state, node, color):
        if state[node] != -1:
            return state[node] == color % 2
        state[node] = color % 2

        for n in graph[node]:
            if not self.valid_color(graph, state, n, color + 1):
                return False

        return True

