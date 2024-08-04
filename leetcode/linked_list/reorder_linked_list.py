# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        # find the mid of list
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        s.next = None

        # reverse right list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # adjust pointers
        first, second = head, prev

        # reorder list
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2