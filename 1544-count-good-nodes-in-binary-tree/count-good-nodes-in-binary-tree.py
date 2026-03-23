# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(maxnode,root):
            if not root:
                return 0 
            if root.val>=maxnode:
                count = 1
            else:
                count = 0
            newmax = max(root.val,maxnode)
            return count + dfs(newmax,root.left) + dfs(newmax,root.right)
        return dfs(float('-inf'),root)   
        
        