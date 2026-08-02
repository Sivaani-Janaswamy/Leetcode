# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isIdentical(s,t):
            if (not s and t) or (not t and s):
                return False
            if not s and not t:
                return True
            return s.val==t.val and isIdentical(s.left,t.left) and isIdentical(s.right,t.right)
        def dfs(node,subRoot):
            if not node:
                return False
            if isIdentical(node,subRoot):
                return True
            return dfs(node.left,subRoot) or dfs(node.right,subRoot)
        return dfs(root,subRoot)
