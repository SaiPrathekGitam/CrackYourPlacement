# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # curr1 = l1
        # curr2 = l2
        # prev1 = None
        # prev2 = None
        # while curr1 or curr2:
        #     if curr1:
        #         temp = curr1.next
        #         curr1.next = prev1
        #         prev1 = curr1
        #         curr1 = temp
        #     if curr2:
        #         temp = curr2.next
        #         curr2.next = prev2
        #         prev2 = curr2
        #         curr2 = temp
        # l1 = prev1
        # l2 = prev2
        # carry = 0
        # ret = ans = ListNode(-1)
        # while l1 or l2 or carry:
        #     if l1:
        #         carry += l1.val
        #         l1 = l1.next
        #     if l2:
        #         carry += l2.val
        #         l2 = l2.next
        #     ans.next = ans = ListNode()
        #     carry, ans.val = divmod(carry, 10)
        # curr1 = ret.next
        # prev1 = None
        # while curr1:
        #     temp = curr1.next
        #     curr1.next = prev1
        #     prev1 = curr1
        #     curr1 = temp
        # curr1 = prev1
        # return curr1
        s1 = 0
        s2 = 0
        while l1: 
            s1 *= 10; 
            s1 += l1.val; 
            l1 = l1.next
        while l2: 
            s2 *= 10; 
            s2 += l2.val; 
            l2 = l2.next
        s3 = s1 + s2
        tail = None
        head = None
        while s3 > 0: head = ListNode(s3 % 10); head.next = tail; tail = head; s3 //= 10
        return head if head else ListNode(0)
