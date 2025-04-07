# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        curr_node=0
        while head:
            curr_node = head.next
            head.next = temp
            temp = head
            head =curr_node
        return temp 