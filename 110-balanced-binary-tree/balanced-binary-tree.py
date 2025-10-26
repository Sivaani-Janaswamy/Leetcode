# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(root):
            if root is None:
                return 0
            leftHeight =  helper(root.left)
            rightHeight = helper(root.right)
            if leftHeight==-1 or rightHeight==-1:
                return -1
            if abs(leftHeight-rightHeight)>1:
                return -1
            height = 1 + max(leftHeight,rightHeight)
            return height
        result = helper(root)
        if result == -1:
            return False
        else:
            return True


        