# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        nums = []
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        return nums
        
        