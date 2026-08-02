# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        hashset = set()
        def dfs(node,k):
            if not node:
                return False
            res = k-node.val
            if res in hashset:
                return True
            hashset.add(node.val)
            return dfs(node.left,k) or dfs(node.right,k)
            
        return dfs(root,k)
