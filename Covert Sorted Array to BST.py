# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        dummy = TreeNode()
        curr = dummy

        def addNodes(nums):
            if not nums:
                return None

            if len(nums) == 1:
                return TreeNode(nums[0])

            l = 0
            r = len(nums) - 1

            if (l + r) % 2 == 1:
                m = ((l + r) // 2) + 1 
            else:
                m = (l + r) // 2

            root = TreeNode(nums[m])
            root.left = addNodes(nums[:m])
            root.right = addNodes(nums[m+1:])

            return root

        curr.left = addNodes(nums)

        return curr.left

        