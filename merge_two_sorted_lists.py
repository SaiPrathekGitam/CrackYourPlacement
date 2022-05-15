class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ans = ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                ans.next = list1
                ans = ans.next
                list1 = list1.next
            else:
                ans.next = list2
                ans = ans.next
                list2 =  list2.next
        if list1: 
            ans.next = list1
        else:
            ans.next = list2
        return head.next
