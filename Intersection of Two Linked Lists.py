# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        countA, countB = 0, 0
        curr = headA
        while curr:
            curr = curr.next
            countA += 1

        curr = headB
        while curr:
            curr = curr.next
            countB += 1
        
        if countA > countB:
            for i in range(countA - countB):
                headA = headA.next
        else:
            for i in range(countB - countA):
                headB = headB.next

        # print(countA, countB, headA.val, headB.val)

        def searchI(headA, headB):
            if headA.next and headB.next:
                res = searchI(headA.next, headB.next)
            elif headA.next:
                res = searchI(headA.next, headB)
            elif headB.next:
                res = searchI(headA, headB.next)
            else:
                if headA == headB:
                    return headA
                else:
                    return None

            if headA == headB:
                return headA
            else:
                return res
        
        return searchI(headA, headB)
        