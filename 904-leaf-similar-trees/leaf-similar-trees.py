# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(seq,root):
            if not root:
                return
            if not root.left and not root.right:
                seq.append(root.val)
                return seq
            dfs(seq,root.left)
            dfs(seq,root.right)
            return seq
        return dfs([],root1)==dfs([],root2)
        