# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        curr = head

        while curr:
            res.append(curr.val)
            curr = curr.next

        l = 0
        r = len(res) - 1

        while l < r:
            if res[l] != res[r]:
                return False

            l += 1
            r -= 1
        
        return True
        