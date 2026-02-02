# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        newSum = targetSum - root.val
        if not root.left and not root.right and newSum==0:
            return True
        return self.hasPathSum(root.left,newSum) or self.hasPathSum(root.right,newSum)
          
        
        
        
        
        
        