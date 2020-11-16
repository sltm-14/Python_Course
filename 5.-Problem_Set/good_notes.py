class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        slef.right = right

    def good_nodes (root,max_node=float('-inf')):
        if root is None:
            return 0
        else:
            is_good = max_node <= root
            left = self.goodNodes(root.left,mx(max_node,root.val))
            right = self.goodNodes(root.left,mx(max_node,root.val))
            return is_good + left + right
