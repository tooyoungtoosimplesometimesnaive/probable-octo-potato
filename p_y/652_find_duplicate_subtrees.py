class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        count = collections.Counter()
        ans = []
        def collect(node):
            if not node:
                return '#'
            tree_repr = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[tree_repr] += 1
            if count[tree_repr] == 2:
                ans.append(node)
            return tree_repr
        
        collect(root)
        return ans
