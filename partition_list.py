class Solution:
    def partition(self, temp: Optional[ListNode], x: int) -> Optional[ListNode]:
        ret = p1 = ListNode()
        join = p2 = ListNode()
        while temp:
            if temp.val<x:
                p1.next = p1 = ListNode(temp.val)
            else:
                p2.next = p2 = ListNode(temp.val)
            temp = temp.next
        p1.next = join.next
        return ret.next
