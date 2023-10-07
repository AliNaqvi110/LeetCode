# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        # Create a dummy node to simplify the code.
        curr = dummy = ListNode(0)
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # If one of the lists is not empty, append it to the result.
        if list1 is not None or list2 is not None:
            curr.next = list1 if list1 else list2
        return dummy.next