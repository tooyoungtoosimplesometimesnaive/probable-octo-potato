class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        start_ids = []
        end_ids = []
        return self.get_width(root, 0, 1, start_ids, end_ids)
        
    def get_width(self, root, level_id, node_id, start_ids, end_ids):
        if root == None:
            return 0
        if len(start_ids) == level_id:
            start_ids.append(node_id)
            end_ids.append(node_id)
        else:
            end_ids[level_id] = node_id
        
        current = end_ids[level_id] - start_ids[level_id] + 1
        left = self.get_width(root.left, level_id + 1, node_id * 2, start_ids, end_ids)
        right = self.get_width(root.right, level_id + 1, node_id * 2 + 1, start_ids, end_ids)
        return max(current, left, right)

