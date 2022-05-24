class Solution(object):
    def removeOuterParentheses(self, s):
        c = 0
        ans = ''
        temp = ''
        for i in s:
            if i=='(' and c>0:
                c+=1
                temp+='('
            elif i=='(':
                ans+=temp[1:-1]
                temp = '('
                c+=1
            elif i==')' and c>0:
                c-=1
                temp+=')'
        return ans+temp[1:-1]
                
