# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        def reverseList(head: ListNode) -> ListNode:
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        
        head = reverseList(head)
        curr = head

        i, prev = 1, None
        while curr:
            if i == n:
                # last elem
                if i == 1:
                    head = curr.next
                # other elem
                else:
                    prev.next = curr.next
                curr.next = None
                break
            prev = curr
            curr = curr.next
            i += 1

        return reverseList(head)