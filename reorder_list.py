class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        l = []
        while temp:
            l.append(temp.val)
            temp = temp.next
        i = 0
        ans = []
        while i<len(l)//2:
            ans.append(l[i])
            i+=1
            ans.append(l[-i])

        if len(l)%2!=0:
            ans.append(l[i])
        temp = head
        for i in ans[1:]:
            temp.next = temp = ListNode(i)
