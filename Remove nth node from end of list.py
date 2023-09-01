# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        
        

nums = [1,2,3,4,5]

fi = ListNode(nums[-1])
fo = ListNode(nums[-2], fi)
th = ListNode(nums[-3], fo)
tw= ListNode(nums[-4], th)
on = ListNode(nums[-5], tw)


x = Solution.removeNthFromEnd(fo, fo, 1)
print(x.val)