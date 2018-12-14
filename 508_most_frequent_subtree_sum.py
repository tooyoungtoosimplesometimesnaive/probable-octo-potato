# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.values = collections.defaultdict(int)
        self.max_freq = 0

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.find(root)
        result = []
        for k, v in self.values.items():
            if v == self.max_freq:
                result.append(k)
                
        return result
        
    def find(self, root):
        if root == None:
            return 0
        left = self.find(root.left)
        right = self.find(root.right)
        s = left + right + root.val
        self.values[s] += 1
        self.max_freq = max(self.max_freq, self.values[s])
        return s
        
        
        
