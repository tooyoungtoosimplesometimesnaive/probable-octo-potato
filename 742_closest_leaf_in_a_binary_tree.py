# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        self.dfs(graph, root, None)
        
        #print(graph)
        queue = list(node for node in graph if node and node.val == k)
        
        visited = set(queue)
        
        while queue:
            node = queue.pop(0)
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                else:
                    for n in graph[node]:
                        if n not in visited:
                            visited.add(n)
                            queue.append(n)

    def dfs(self, graph, root, parent):
        if root == None:
            return
        if parent != None:
            graph[parent].append(root)
        graph[root].append(parent)
        self.dfs(graph, root.left, root)
        self.dfs(graph, root.right, root)

