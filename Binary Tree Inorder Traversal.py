# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []

        def inOrder(n):
            if not n:
                return

            
            inOrder(n.left)
            vals.append(n.val)
            inOrder(n.right)

        
        inOrder(root)
        return vals
        