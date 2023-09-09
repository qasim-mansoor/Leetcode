# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and head.next:
            t = head
            h = head.next

            while h and h.next:
                if h == t:
                    return True
                else:
                    t = t.next
                    h = h.next.next
            return False
        else:
            return False
