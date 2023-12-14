#! using merge sort algorithm in this problem

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case
        if not head or not head.next:
            return head

        # splitting into two lists
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
        
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, list1, list2):
        dummy = tail = ListNode()
        
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next