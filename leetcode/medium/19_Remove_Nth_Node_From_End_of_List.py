class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next

        return dummy.next