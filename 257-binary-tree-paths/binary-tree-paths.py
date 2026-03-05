# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result = []
        def dfs(node,path,result):
            if not node:
                return
            if path == "":
                path=str(node.val)
            else: 
                path = path + "->" + str(node.val)
            if not node.left and not node.right:
                result.append(path)
                return
            dfs(node.left,path,result)
            dfs(node.right,path,result)
        dfs(root,"",result)
        return result

            
            

        