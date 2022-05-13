class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = 1
        ans = ''
        while i<=min(len(a) , len(b)):
            s = carry+int(a[-i])+int(b[-i])
            i+=1
            if s == 0:
                carry = 0
                ans+='0'
            elif s == 1:
                carry = 0
                ans+='1'
            elif s == 2:
                carry = 1
                ans+='0'
            else:
                carry = 1
                ans+='1'
        while i<=len(a):
            s = carry+int(a[-i])
            i+=1
            if s == 0:
                carry = 0
                ans+='0'
            elif s == 1:
                carry = 0
                ans+='1'
            elif s == 2:
                carry = 1
                ans+='0'
            else:
                carry = 1
                ans+='1'
        while i<=len(b):
            s = carry+int(b[-i])
            i+=1
            if s == 0:
                carry = 0
                ans+='0'
            elif s == 1:
                carry = 0
                ans+='1'
            elif s == 2:
                carry = 1
                ans+='0'
            else:
                carry = 1
                ans+='1'
        ans+=str(carry)    
        return str(int(ans[::-1]))

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         carry = 0
#         result = ''

#         a = list(a)
#         b = list(b)

#         while a or b or carry:
#             if a:
#                 carry += int(a.pop())
#             if b:
#                 carry += int(b.pop())

#             result += str(carry %2)
#             carry //= 2

#         return result[::-1]
