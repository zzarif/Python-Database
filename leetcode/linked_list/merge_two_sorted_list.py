# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        prev = head = None

        if list1 and list2:
            head = list1 if list1.val < list2.val else list2
        else:
            head = list1 or list2

        while list1 and list2:

            if list1.val < list2.val:
                if prev:
                    prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                if prev:
                    prev.next = list2
                prev = list2
                list2 = list2.next

        if prev:
            prev.next = list1 or list2

        return head