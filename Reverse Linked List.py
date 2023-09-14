# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            h1 = head
            h2 = head.next
            h3 = h2.next
            h1.next = None
            while h3:
                h2.next = h1

                h1 = h2
                h2 = h3
                h3 = h2.next

            h2.next = h1
        else:
            h2 = head

        return h2

