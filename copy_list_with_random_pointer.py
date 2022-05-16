class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        ret = ans = Node(-1)
        dic = {}
        while temp:
            ans.next = ans = Node(temp.val, temp.next)
            dic[temp] = ans
            temp = temp.next
        ans = ret
        temp = head
        while ans.next:
            if temp.random in dic:
                ans.next.random = dic[temp.random]
            ans = ans.next
            temp = temp.next
        return ret.next
